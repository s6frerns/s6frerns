import numpy as np
import scipy.optimize as so
#import scipy.special.gammainc
import matplotlib.pyplot as plt
import pandas as pd
from numpy import sin, cos, sqrt


#####################################################
"""
Often Used:

data = np.array(np.loadtxt('datei.txt',usecols=(0,1,2,3))).transpose()
print("Raw Data: ", data)

fig = plt.figure()
ax1 = fig.add_subplot(111)
fit(fit_func, x ,y ,x_err ,y_err, ax1)

ax1.legend()

ax1.set_title()
ax1.set_xlabel(r"")
ax1.set_ylabel(r"")

"""
#####################################################
"""
Less Used:

# scientific notation in labeling
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0, 0), useMathText=True)
"""

#####################################################
##################from fit import *###################################
"""
Useful Functions
"""


def cosd(x): return np.cos(np.deg2rad(x))


def sind(x): return np.sin(np.deg2rad(x))


def intervall(array, res=100):
    return np.arange(np.min(array), np.max(array), (np.max(array) - np.min(array)) / res)


def invert_array(array):
    return [not a for a in array]


def pos_to_boolean(pos, length):
    b = [False]*length
    for p in pos:
        b[p] = True
    return b


#####################################################
#####################################################
"""
Fit Functions
"""


def polynom2(x, a, b, c):
    return(c*x**2 + b*x + a)


def polynom3(x, a, b, c, d):
    return(d*x**3 + c*x**2 + b*x + a)


def polynom4(x, a, b, c, d, e):
    return(e*x**4 + d*x**3 + c*x**2 + b*x + a)


def polynom5(x, a, b, c, d, e, f):
    return(f*x**5 + e*x**4 + d*x**3 + c*x**2 + b*x + a)

# def n_polynom(x, *args):
#     return np.poly1d(*args)(x)


def const(x, a): return np.ones(len(x))*a


def lin(x, m, n): return x*m+n


def origin_lin(x, m): return x*m


def resonanz(x, a, b, c, d): return a/np.sqrt(b+(x*c-1/(x*d)**2))

def sinus(x, a, b, c,d): return 20*a*np.sin(b/20*x+d)+c

def Gauss(x, a, x0): return a * np.exp(-(x - x0)**2 / (2 * 2**2))

#####################################################
#####################################################
x = np.arange(10)
y = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1])

x_err = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
y_err = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

"""
Fit

Use as:
fit(fit_func, x ,y ,x_err ,y_err, ax)
"""






def fit(fit_func, x, y, x_err, y_err, ax=None, printing=True, err_plot=False, label=None, include=None, exclude=None,
        linewidth=1, bar_color='darkorange', fit_color='royalblue', fill_err=False, capsize=None, mark_include=None,
        mark_exclude=None, plot_fit=True, linestyle=None, chi_square=True):

    # Check if array
    if (type(x_err) != np.ndarray):
        x_err = np.array([x_err]*len(x))
    if (type(y_err) != np.ndarray):
        y_err = np.array([y_err] * len(y))

    # Intervall, sigma
    x_intervall = intervall(x)

    sigma = y_err
    if((sigma == 0).all()):
        sigma = np.ones(len(sigma)) * y * 10 ** -5

    # specify values to include/ exclude from fitting
    if (exclude != None):
        include = invert_array(exclude)
    elif (include == None):
        include = [True] * len(x)
    else:
        exclude = invert_array(include)

    # Actual fit, only include specified values
    popt, pcov = so.curve_fit(
        fit_func, x[include], y[include], sigma=sigma[include], absolute_sigma=True)
    perr = sqrt(np.diag(pcov))

    # Print to console
    if (printing):
        print(fit_func)
        print(pd.DataFrame(
            np.array([popt, perr]).transpose(), columns=["Params", "Errs"]))

    # Plotting
    if (ax != None):
        if(capsize == None):
            capsize = linewidth * 2
        else:
            capsize = 0
        ax.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='none',
                    color=bar_color, linewidth=linewidth, capsize=capsize, label=label)
        if(plot_fit):
            ax.plot(x_intervall, fit_func(x_intervall, *popt),
                    color=fit_color, linestyle=linestyle)
            # Plot errors of the fit
            if (err_plot):
                ax.plot(x_intervall, fit_func(x_intervall, *(popt+perr)),
                        color=fit_color, linestyle='dashed', linewidth=linewidth)
                ax.plot(x_intervall, fit_func(x_intervall, *(popt-perr)),
                        color=fit_color, linestyle='dashed', linewidth=linewidth)
                if (fill_err):
                    ax.fill_between(x_intervall, fit_func(x_intervall, *(popt+perr)),
                                    fit_func(x_intervall, *(popt - perr)), color=fit_color, alpha=0.1)
            # Mark included/ excluded values
            if (mark_include != None):
                ax.scatter(x[include], y[include],
                           color='red', marker=mark_include, alpha=1, linewidth=linewidth)
            if (mark_exclude != None):
                ax.scatter(x[exclude], y[exclude],
                           color='red', marker=mark_exclude, alpha=1, linewidth=linewidth)
    if(label != None):
        ax.legend()

    # Chi Square Test
    """if (chi_square):
        chi_sq = chi_square(len(x),
                            fit_func(x, *popt),
                            y,
                            y_err)
        print("ChiSquare=", chi_sq[0], " with prob ", chi_sq[1])"""
    # Return parameters
    return (popt, perr)


#####################################################
#####################################################
"""
Chi Square Test
    k: number of params
    model_vals: model values
    exp_vals: experimental values
    sigma: errors of experimental values
"""


def chi_square(k, model_vals, exp_vals, sigma):
    chi_sq = np.sum((exp_vals - model_vals) ** 2 / sigma ** 2)
    p = gammainc(k / 2, chi_sq / 2)
    return (chi_sq, p)


#####################################################
#####################################################
"""
Write to csv

Use as:
write_to_csv(('data'), (data), 'file.csv')
"""


def write_to_csv(headers, values, filename):
    header = ''
    for h in headers:
        header += h + ','
    header = header[:-1]
    np.savetxt(filename+".csv", np.transpose(values),
               delimiter=",", header=header)


def write_to_csv_new(headers, values, filename, printing=False):
    values = list(values)
    headers = list(headers)
    l = len(values[0])
    for i, v in enumerate(values):
        if (type(v) != np.ndarray and type(v) != list):
            # print("Correcting length of ", headers[i])
            values[i] = np.array([v] * l)
        if (i % 3 == 0):
            values.insert(i+1, np.array(['±'] * l))
            headers.insert(i + 1, "")
            headers[i+2] = ""
    values = np.array(values)
    headers = np.array(headers)
    values = np.concatenate(([headers], values.transpose()), axis=0)
    if(printing):
        print(pd.DataFrame(values))
    # for v in values:
    #     print(len(v), type(v), v)
    header = ''
    for i, h in enumerate(headers):
        header += h + ','
    header = header[:-1]
    np.savetxt(filename+".csv", values,
               delimiter=",", fmt="%s", encoding='utf8')


#####################################################
#####################################################
"""
Old
"""

""" linear chi square fit, returns (m, n, m_sigma, n_sigma) """


def fit_old(x, y, sigma):
    # varianzgewichteter Mittelwert
    def var_mean(values, sigma):
        return np.sum(values/(sigma**2))/np.sum(1/(sigma**2))

    # Calculate mean values
    x_m = var_mean(x, sigma)
    y_m = var_mean(y, sigma)
    sigma_m = len(sigma)/np.sum(1/(sigma**2))
    xy_m = var_mean(x*y, sigma)
    xsq_m = var_mean(x*x, sigma)
    # print(x_m, y_m, sigma_m, xy_m, xsq_m)

    # Calculate m, n
    m = (xy_m-x_m*y_m)/(xsq_m-x_m**2)
    n = (xsq_m*y_m-x_m*xy_m)/(xsq_m-x_m**2)

    # Calculate uncertainties
    m_sigma = sigma_m/(len(x)*(xsq_m-x_m**2))
    n_sigma = np.sqrt(xsq_m*m_sigma)
    m_sigma = np.sqrt(m_sigma)
    return (m, n, m_sigma, n_sigma)

#####################################################
#####################################################

# arr: 2d-array with values for table, not transposed; precision: tuple with decimals for each column


def latex_tabular(arr, precision, firstcol=False, tutor="none"):
    # firstcol=True will add a column at the very left with the number of the row
    header = "\\begin{tabular}{|"
    if firstcol == True:
        header += "c|"
    for j in range(int(.5*arr.shape[1])):
        header += "rcl|"

    header += "} \n\\hline\n"

    if firstcol == True:
        header += "\#&"

    for j in range(int(.5*arr.shape[1])):
        header += "\\multicolumn{3}{|c|}{NAME?} &"

    header = header[:-1] + "\\\ \n\\hline\n"

    table = ""
    for i in range(arr.shape[0]):
        row = ""
        if firstcol == True:
            row += r"${}$& ".format(i+1)
        for j in range(int(.5*arr.shape[1])):
            row += "$" + r"{:.{decimals}f}".format(arr[i][2*j], decimals=precision[2*j]) + "$ & \t $\pm$ & \t $" + \
                r"{:.{decimals}f}".format(
                    arr[i][2*j+1], decimals=precision[2*j+1]) + "$ &\t"

        table += row[:-3] + "\\\ \n"

    end = "\hline\n\\end{tabular}"

    return header + table + end


mean = sum(x * y) / sum(y)
sigma = np.sqrt(sum(y * (x - mean)**2) / sum(y))
print(sigma)
fig = plt.figure()
ax = fig.add_subplot(111)
fit(Gauss, y, x, 0,0, ax)
plt.show()
