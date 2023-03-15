# labels each container in a stacked barplot
for container in ax.containers:
    ax.bar_label(container)
    


# Labels the topline count
ax.bar_label(ax.containers[-1])
