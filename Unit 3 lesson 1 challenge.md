

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

%matplotlib inline
```

1. Greg was 14, Marcia was 12, Peter was 11, Jan was 10, Bobby was 8, and Cindy was 6 when they started playing the Brady kids on The Brady Bunch. Cousin Oliver was 8 years old when he joined the show. What are the mean, median, and mode of the kids' ages when they first appeared on the show? What are the variance, standard deviation, and standard error?

mean <br/>
(14 + 12 + 11 + 10 + 8 + 6)/ 6 = <br/>
10.1667

median <br/>
6 8 10 11 12 14 <br/>
(10 + 11)/2 = <br/>
10.5

mode <br/>
6 8 10 11 12 14 <br/>
No Mode

variance <br/>
sum((x - 10.1667) ** 2) / (5)  | x = 6, 8, 10, 11, 12, 14 <br/>
6.8

standard deviation <br/>
6.8 ** .5 = <br/>
2.6

standard error <br/>
2.6 / (6 ** 0.5) = <br/>
1.17





```python
df = pd.DataFrame([6, 8, 10, 11, 12, 14])
```


```python
np.mean(df)
```




    0    10.166667
    dtype: float64




```python
np.median(df)
```




    10.5




```python
statistics.mode(df)
```




    0




```python
np.var(df)
```




    0    6.805556
    dtype: float64




```python
np.std(df)
```




    0    2.608746
    dtype: float64




```python
np.std(df ,ddof=1) / np.sqrt(len(df))
```




    0    1.166667
    dtype: float64




```python

```

2. Using these estimates, if you had to choose only one estimate of central tendency and one estimate of variance to describe the data, which would you pick and why?

I'd use the mean because there isn't a strong prescence of outliers (meaning there's no real need to use the median).
I'd use the standard deviation because it has more interpretable statistical implications especially when paired with the mean.


3. Next, Cindy has a birthday. Update your estimates- what changed, and what didn't?

mean <br/>
(14 + 12 + 11 + 10 + 8 + 7)/ 6 = <br/>
10.33

median <br/>
7 8 10 11 12 14 <br/>
(10 + 11)/2 = <br/>
10.5

mode <br/>
7 8 10 11 12 14 <br/>
No Mode

variance <br/>
sum((x - 10.33) ** 2) / (5)  | x = 7, 8, 10, 11, 12, 14 <br/>
5.56

standard deviation <br/>
6.8 ** .5 = <br/>
2.36

standard error <br/>
2.6 / (6 ** 0.5) = <br/>
1.05

The mean, variance, standard deviation, and standard error changed.



```python
df2 = pd.DataFrame([7, 8, 10, 11, 12, 14])
```


```python
np.mean(df2)
```




    0    10.333333
    dtype: float64




```python
np.median(df2)
```




    10.5




```python
statistics.mode(df2)
```




    0




```python
np.var(df2)
```




    0    5.555556
    dtype: float64




```python
np.std(df2)
```




    0    2.357023
    dtype: float64




```python
np.std(df2 ,ddof=1) / np.sqrt(len(df2))
```




    0    1.054093
    dtype: float64



4. Nobody likes Cousin Oliver. Maybe the network should have used an even younger actor. Replace Cousin Oliver with 1-year-old Jessica, then recalculate again. Does this change your choice of central tendency or variance estimation methods?

mean <br/>
(14 + 12 + 11 + 10 + 1 + 7)/ 6 = <br/>
9.16

median <br/>
7 1 10 11 12 14 <br/>
(10 + 11)/2 = <br/>
10.5

mode <br/>
7 1 10 11 12 14 <br/>
No Mode

variance <br/>
sum((x - 10.1667) ** 2) / (5)  | x = 7, 1, 10, 11, 12, 14 <br/>
17.8

standard deviation <br/>
6.8 ** .5 = <br/>
4.22

standard error <br/>
2.6 / (6 ** 0.5) = <br/>
1.89

I would switch to using the median since it is less likely to be affected by the new outlier.



```python
df3 = pd.DataFrame([7, 1, 10, 11, 12, 14])
```


```python
np.mean(df3)
```




    0    9.166667
    dtype: float64




```python
np.median(df3)
```




    10.5




```python
statistics.mode(df3)
```




    0




```python
np.var(df3)
```




    0    17.805556
    dtype: float64




```python
np.std(df3)
```




    0    4.219663
    dtype: float64




```python
np.std(df3 ,ddof=1) / np.sqrt(len(df3))
```




    0    1.887091
    dtype: float64




```python

```

5. On the 50th anniversary of The Brady Bunch, four different magazines asked their readers whether they were fans of the show. The answers were: TV Guide 20% fans Entertainment Weekly 23% fans Pop Culture Today 17% fans SciPhi Phanatic 5% fans <br/>
Based on these numbers, what percentage of adult Americans would you estimate were Brady Bunch fans on the 50th anniversary of the show?

median <br/>
20, 23, 17, 5 <br/>
(23 +17) / 2 = <br/>
18.5



```python
df4 = pd.DataFrame([20, 23, 17, 5])
```


```python
np.median(df4)
```




    18.5




```python

```
