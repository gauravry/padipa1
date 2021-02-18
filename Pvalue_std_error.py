import math

x = int(input())
n = int(input())
mu = float(input())
sigma = float(input())

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

req_wt = x/n

SE = (mu - req_wt)/(sigma/math.sqrt(n))


def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

def cdf2(x, mu, sigma):
    Z = (x - mu)/(sigma/math.sqrt(n))
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

#cdf2 = lambda x: 0.5*(1 + math.erf((sigma/math.sqrt(n))/(math.sqrt(2))))    

#print(round(cdf(x, mu_sum, sigma_sum), 4))
print(round(cdf2(req_wt, mu, sigma), 4))
