import numpy as np


def autocorrelation_function(series, max_lags=20):
    """Calculates the autocorrelation function (ACF).
       Args:
           series: list of values (the time series).
           max_lags: maximum number of lags calculated.
       Returns:
           np.Array with the autocorrelation function.

    """
    lag_list = list(range(max_lags))
    autocovariances = []
    for lag in lag_list:  # Calculating autocovariances for each lag
        autocovariances.append(autocovariance(series, lag))

    autocorrelations = np.divide(autocovariances, autocovariances[0])  # Directly from the formula
    return autocorrelations
    

def autocovariance(series, lag):
    """Calculates the autocovariance for a series and a given lag.
       Args:
           series: list of values (the time series).
           lag: number of periods to lag the series.
       Returns:
           np.float autocovariance value

    """
    len_series = len(series)
    mean_series = np.mean(series)
    
    covariances = []
    for index in range(lag, len_series):
        # Simple covariance calculation. This can be easily replaced with np.cov, 
        # but it is educational to calculate it ourselves.
        covariance = (series[index] - mean_series)*(series[index - lag] - mean_series)
        covariances.append(covariance)

    autocovariance = np.sum(covariances) / len_series
    return autocovariance
