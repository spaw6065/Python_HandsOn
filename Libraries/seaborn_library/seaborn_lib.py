import pandas as pd
import seaborn as sns
import numpy as np


######################################################################
### Plotting with relative data                                   #
######################################################################
tips = pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/tips.csv")
sns.set()

sns.load_dataset("tips")

# print(tips.get("total_bill"))

sns.relplot(x="total_bill",
            y="tip",
            col="time",
            hue="smoker",
            size="size",
            style="smoker",
            data=tips)
sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips);


#prepare a dataframe and plot using lineplot
df = pd.DataFrame(time=np.arange(500),
                  value=np.random.randn().cumsum())
g=sns.relplot(x="time",y="value",kind="line",data=df)
g.fig.autofmt_xdate()

#disable the default sort
df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0),
                  columns=["x", "y"])
sns.relplot(x="x", y="y", sort=False, kind="line", data=df);

fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri);

#Without confidence interval
fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri,ci=None);

sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);

#to turn off the estimator
sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);

sns.relplot(x="timepoint", y="signal", hue="event", kind="line", data=fmri);

#to plot markers for identification of subset
sns.relplot(x="timepoint",y="signal",hue="region",style="event",dashes=False,markers=True,kind="line",data=fmri)

emp_df = pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/employee.csv")
print(emp_df)

sns.relplot(x="empdeptname",y="empsalary",hue="empdeptname",style="empdeptname",kind="scatter",data=emp_df)

sns.relplot(x="timepoint", y="signal", hue="region",
            units="subject", estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));

dots = pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/dots.csv")

print(dots)

sns.relplot(x="time",y="firing_rate",hue="coherence",style="choice",kind="line",data=dots)


##changing the color of the data presentation
palette = sns.cubehelix_palette(light=.8, n_colors=10)
sns.relplot(x="time",
            y="firing_rate",
            hue="coherence",
            style="choice",
            kind="line",
            palette=palette,
            data=dots)

##use size to increase the visibility of the lines plotted
sns.relplot(x="timepoint", y="signal", hue="subject",
    col="region", row="event", height=3,
    kind="line", estimator=None, data=fmri);

#plot multiple facets/graph based on column and number of individual graphs
sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=3, aspect=.50, linewidth=2.5,
            kind="line", data=fmri.query("region == 'frontal'"));


######################################################################
### Plotting with categorical data                                   #
######################################################################
# Categorical scatterplots:
#     stripplot() (with kind="strip"; the default)
#     swarmplot() (with kind="swarm")
# Categorical distribution plots:
#     boxplot() (with kind="box")
#     violinplot() (with kind="violin")
#     boxenplot() (with kind="boxen")
# Categorical estimate plots:
#     pointplot() (with kind="point")
#     barplot() (with kind="bar")
#     countplot() (with kind="count")
import matplotlib.pyplot as plt
sns.set(style="ticks",color_codes=True)
tips=pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/tips.csv")

print(tips)
sns.catplot(x="day",y="tip",data=tips)
sns.catplot(x="day",y="tip",jitter=False,data=tips)

##beesswarn by setting kind="swarm"
sns.catplot(x="day",y="tip",kind="swarm",data=tips)
sns.catplot(x="day",y="tip",kind="swarm",hue="smoker",data=tips.query("day=='Sun'"))

#order the x-axis elements usig list
sns.catplot(x="day", y="tip", order=["Sun","Mon","Tue","Wed","Thur","Fri","Sat"], data=tips);

#When the data is clumpsy and we need to represent on the graph use box scatter option
sns.catplot(x="day", y="tip", kind="box", data=tips);

##Use different kind
sns.catplot(x="day", y="tip", kind="strip",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);
sns.catplot(x="day", y="tip", kind="violin",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);
sns.catplot(x="day", y="tip", kind="boxen",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);
sns.catplot(x="day", y="tip", kind="point",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);
sns.catplot(x="day", y="tip", kind="bar",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);

# for count we need to set one of the axis as None
sns.catplot(x="day", y=None, kind="count",hue="smoker",order=["Thur","Fri","Sat","Sun"], data=tips);

##Boxen plot
##load the diamond dataset
diamonds=pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/diamonds.csv")
sns.load_dataset(diamonds)
sns.catplot(x="color",y="price",kind="boxen",data=diamonds.sort_values("color"));
sns.catplot(x="cut",y="price",kind="boxen",data=diamonds.sort_values("color"));

##palette = pastel is to reduce the color intensity and inner stick is to mark the widht length
## split=True splits based on the hue part
sns.catplot(x="day", y="total_bill", hue="sex",
            kind="violin", inner="stick", split=True,
            palette="pastel", data=tips);

## Using barplot to plot the bars instead of scatterplot and swarmplot
titanic=sns.load_dataset("titanic")
sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic)

##Violinplot
sns.violinplot(x="day",y="total_bill",data=tips)

######################################################################
### Plotting distribution of a dataset                               #
######################################################################
##For univariate we can use kdeplot and for bivariate we can use kdeplot,joinplot and pairplot
## to plot the relationship between variables
x=np.random.normal(4,2,size=40)
sns.kdeplot(x,shade=True,kernel="gau",bw="scott",gridsize=100,cut=3,clip=None,legend=True)
sns.kdeplot(x,bw=0.2,label="bw:0.2")

##bandwidth shows the estimation with respect to the smallest and largest values in the dataset

x=np.random.gamma(6,2,200)
sns.distplot(x,kde=False)

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

sns.scatterplot(x="x",y="y",data=df)
sns.jointplot(x="x",y="y",data=df)

x, y = np.random.multivariate_normal(mean, cov, 1000).T
#style must be one of white, dark, whitegrid, darkgrid, ticks
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind="hex", color="k");

sns.jointplot(x="x",y="y",data=df,kind="kde")

f, ax = plt.subplots(figsize=(6, 6))
cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
sns.kdeplot(df.x, df.y, cmap=cmap, n_levels=60, shade=True);

iris=sns.load_dataset("iris")
sns.pairplot(iris)

sns.pairplot(iris,hue="species")

##Analysing the data using linear model and regression model techniques
## methods used here are lmplot() and regplot()
sns.lmplot(x="total_bill",y="tip",hue="smoker",data=tips)

sns.lmplot(x="size",y="tip",data=tips,x_estimator=np.mean)

anscombe=sns.load_dataset("sns")
sns.lmplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
           ci=None, scatter_kws={"s": 80});

##User defined dataframe
emp_df=pd.read_csv("C:/Users/SumitPawar/Python_classes/GitCode/Python_Practice/datasets/seaborn-data/employee.csv")
sns.lmplot(x="empid",y="empsalary",hue="empdeptname",data=emp_df)

#residplot
sns.residplot(x="x", y="y", data=anscombe.query("dataset == 'I'"),
              scatter_kws={"s": 80});

##Creating multi plot grids
tips=sns.load_dataset("tips")
#Below line creates the empty graph
g=sns.FacetGrid(tips,col="time")

#Below line plots the Facetgrid on to the graph
g.map(plt.hist,"tip")

g=sns.FacetGrid(tips,col="time",hue="smoker")
g.map(plt.hist,"tip")


g=sns.FacetGrid(tips,col="time",hue="smoker")
g.map(plt.scatter,"total_bill","tip",alpha=.7)

g=sns.FacetGrid(data=tips,row="smoker",col="time",margin_titles=True)
g.map(sns.regplot,"total_bill","tip",color=".3",fit_reg=False,x_jitter=.1)

pal = dict(Lunch="seagreen", Dinner="gray")
g = sns.FacetGrid(tips, hue="time", palette=pal, height=5)
g.map(plt.scatter, "total_bill", "tip", s=50, alpha=.7, linewidth=.5, edgecolor="white")


##Changing the content of the x and y axis
with sns.axes_style("white"):
    g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, height=2.5)
g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=.5);
g.set_axis_labels("Total bill (US Dollars)", "Tip");
g.set(xticks=[10, 30, 50], yticks=[2, 6, 10]);
g.fig.subplots_adjust(wspace=.02, hspace=.02);

