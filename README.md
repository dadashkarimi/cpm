# cpm
connectome-based predictive modeling

This is a repository for connectome-based predictive modeling based on ridge regression. Original implementation based in python, MATLAB, and C++ is provided in [YaleMRRC](https://github.com/YaleMRRC/CPM).

## Configuration file
In this file all you need is to provide appropriate directories for your connectomes, behavioral values, and model.


```
[default]
model=cpm
database=abcd
task=rest1
iterations=10
   
[behavior]
abcd=/home/javid/datasets/data/abcd/all_behav.csv
  
[path]
abcd=/data_dustin/store4/Templates/ABCD

```
