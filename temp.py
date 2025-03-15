'''
Block:
Define our MarkovSwitch2 (2 Regimes) class.
'''
# not important
import sys, os
from pathlib import Path
import csv

# We append the repository path to the sys.path so that we can import packages easily.
#sys.path.append(os.path.expandvars('D:\Projects\Regime_Switch'))

# utils
import numpy as np, pandas as pd
from datetime import datetime, date, timedelta

# statsmodels for MarkovAutoregression
import statsmodels.api as sm

# plotting tools
import matplotlib.pyplot as plt
from matplotlib import style, cm
style.use('dark_background')

# ccxt as our currency-fetching library
import ccxt

# arch for the GARCH model
from arch import arch_model
from arch.univariate import GARCH

class MarkovSwitch2:
    
    def _defineParams(self, dta):
        # Define the model:
        self.k = 2
        self.model = sm.tsa.MarkovRegression(dta, 
                                        k_regimes=self.k,
                                        trend='nc', 
                                        switching_variance=True)
        print("Model Parameter's defined.")

    def _fitModel(self, dta):
        
        np.random.seed(33)
        
        self._defineParams(dta.forecast_vol)

        # Fit model:
        self.result = self.model.fit()

        # Summary of model:
        print(self.result.summary())

        # Get probabilities of the respective regimes.
        dta['FilteredProbs1'] = self.result.filtered_marginal_probabilities[0]
        dta['SmoothedProbs1'] = self.result.smoothed_marginal_probabilities[0]
        dta['FilteredProbs2'] = self.result.filtered_marginal_probabilities[1]
        dta['SmoothedProbs2'] = self.result.smoothed_marginal_probabilities[1]
        
        
    def _plotFiltered(self, dta, saveDir=''):

        dta['date'] =  range(1, len(dta) + 1)

        # Create the figure:
        f1, ax = plt.subplots(self.k + 2, figsize = (19, 15))

        # Create the plots:
        ax[0].plot(dta.date, dta.FilteredProbs1,label='Low-vol')
        ax[0].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].legend(loc='best')

        ax[1].plot(dta.date, dta.FilteredProbs2, label='High-vol')
        ax[1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].legend(loc='best')
        
        ax[self.k].plot(dta.date,dta.returns,label='Returns',color='gold',linewidth=2)
        ax[self.k].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].set_ylabel('Returns', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].legend(loc='best')

        ax[self.k+1].plot(dta.date,dta.close,label='Close Price',color='gold',linewidth=2)
        ax[self.k+1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].set_ylabel('Close price', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].legend(loc='best')

        plt.grid(linestyle='dotted')
        plt.subplots_adjust(left=0.1, bottom=0.20, right=0.95, top=0.95, wspace=0.2, hspace=0)
        f1.suptitle('Filtered Probabilities of GARCH-Vol for BTC/USD')


        # PNG:
        plt.savefig(saveDir + f'/visuals/MSGARCH_2_Filtered_BTCUSD.png')

        plt.show()
            
    def _plotSmoothed(self, dta, saveDir=''):

        dta['date'] =  range(1, len(dta) + 1)

        # Create the figure:
        f1, ax = plt.subplots(self.k + 2, figsize = (19,15))

        # Create the plots:
        # NOTE: CHANGE THE AXIS NUMBER AND COMMENT THE PLOT LINES YOU DON'T WANT TO PLOT.
        ax[0].plot(dta.date, dta.SmoothedProbs1, label='Low-vol')
        ax[0].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].legend(loc='best')

        ax[1].plot(dta.date,dta.SmoothedProbs2, label='High-vol')
        ax[1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].legend(loc='best')
        
            
        ax[self.k].plot(dta.date,dta.returns,label='Returns',color='gold',linewidth=2)
        ax[self.k].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].set_ylabel('Returns', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].legend(loc='best')
        

        ax[self.k+1].plot(dta.date, dta.close,label='Close Price',color='gold',linewidth=2)
        ax[self.k+1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].set_ylabel('Close price', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].legend(loc='best')
        

        plt.grid(linestyle='dotted')
        plt.subplots_adjust(left=0.1, bottom=0.20, right=0.95, top=0.95, wspace=0.2, hspace=0)
        f1.suptitle('Smoothed Probabilities of GARCH-Vol for BTC/USD')

        # PNG:
        plt.savefig(saveDir + f'/visuals/MSGARCH_2_Smoothed_BTCUSD.png')

        plt.show() 
            

class MarkovSwitch3:
    
    def _defineParams(self, dta):
        # Define the model:
        self.k = 3
        self.model = sm.tsa.MarkovRegression(dta, 
                                        k_regimes=self.k,
                                        trend='nc', 
                                        switching_variance=True)
        print("Model Parameter's defined.")

    def _fitModel(self, dta):
        
        np.random.seed(33)
        
        self._defineParams(dta.forecast_vol)

        # Fit the model:
        self.result = self.model.fit(maxiter=200)

        # Summary of model:
        print(self.result.summary())

        # Get probabilities of the respective regimes.
        dta['FilteredProbs1'] = self.result.filtered_marginal_probabilities[0]
        dta['SmoothedProbs1'] = self.result.smoothed_marginal_probabilities[0]
        
        dta['FilteredProbs2'] = self.result.filtered_marginal_probabilities[1]
        dta['SmoothedProbs2'] = self.result.smoothed_marginal_probabilities[1]
        
        dta['FilteredProbs3'] = self.result.filtered_marginal_probabilities[2]
        dta['SmoothedProbs3'] = self.result.smoothed_marginal_probabilities[2]

        
    def _plotFiltered(self, dta, saveDir=''):

        dta['date'] =  range(1, len(dta) + 1)

        # Create the figure:
        f1, ax = plt.subplots(self.k + 2, figsize = (19, 15))

        # Create the plots:
        ax[0].plot(dta.date, dta.FilteredProbs1,label='Low-Vol')
        ax[0].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].legend(loc='best')

        ax[1].plot(dta.date, dta.FilteredProbs2, label='Medium-Vol')
        ax[1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].legend(loc='best')

        ax[2].plot(dta.date, dta.FilteredProbs3, label='High-Vol')
        ax[2].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[2].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[2].legend(loc='best')
        
        ax[self.k].plot(dta.date, dta.returns, label='Returns',color='gold',linewidth=2)
        ax[self.k].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].set_ylabel('Returns', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].legend(loc='best')

        ax[self.k+1].plot(dta.date, dta.close, label='Close Price',color='gold',linewidth=2)
        ax[self.k+1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].set_ylabel('Close price', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].legend(loc='best')

        plt.grid(linestyle='dotted')
        plt.subplots_adjust(left=0.1, bottom=0.20, right=0.95, top=0.95, wspace=0.2, hspace=0)
        f1.suptitle('Filtered Probabilities of GARCH-Vol for BTC/USD')


        # In PNG:
        plt.savefig(saveDir + f'/visuals/MSGARCH_3_Filtered_BTCUSD.png')

        plt.show()
            
    def _plotSmoothed(self, dta, saveDir=''):

        dta['date'] =  range(1, len(dta) + 1)

        # Create the figure:
        f1, ax = plt.subplots(self.k + 2, figsize = (19, 15))

        # Create the plots:
        # NOTE: CHANGE THE AXIS NUMBER AND COMMENT THE PLOT LINES YOU DON'T WANT TO PLOT.
        ax[0].plot(dta.date, dta.SmoothedProbs1, label='Low-Volatility Regime')
        ax[0].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[0].legend(loc='best')

        ax[1].plot(dta.date,dta.SmoothedProbs2, label='Medium-Volatility Regime')
        ax[1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[1].legend(loc='best')


        ax[2].plot(dta.date,dta.SmoothedProbs3, label='High-Volatility Regime')
        ax[2].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[2].set_ylabel('Probabilities', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[2].legend(loc='best')
            
        ax[self.k].plot(dta.date,dta.returns,label='Returns',color='gold',linewidth=2)
        ax[self.k].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].set_ylabel('Returns', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k].legend(loc='best')

        ax[self.k+1].plot(dta.date,dta.close,label='Close Price',color='gold',linewidth=2)
        ax[self.k+1].set_xlabel('Observations', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].set_ylabel('Close price', horizontalalignment='center', verticalalignment='center', fontsize=12, labelpad=20)
        ax[self.k+1].legend(loc='best')
        

        plt.grid(linestyle='dotted')
        plt.subplots_adjust(left=0.1, bottom=0.20, right=0.95, top=0.95, wspace=0.2, hspace=0)
        f1.suptitle('Smoothed Probabilities of GARCH-Vol for BTC/USD')

        # In PNG:
        plt.savefig(saveDir + f'/visuals/MSGARCH_3_Smoothed_BTCUSD.png')

        plt.show()
