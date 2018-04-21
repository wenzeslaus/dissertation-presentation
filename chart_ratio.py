#!/usr/bin/python

import matplotlib.pyplot as plt


def format_label(value):
    return '{:0.0f}%'.format(value)


fig, ax = plt.subplots()
ax.axis('equal')

values = [26, 74]
text_labels = ['reproducible', 'irreproducible']
colors = ['#6D9CCE', '#F13F52']

width = 0.5
label_position = 1 - width / 2
start_angle = 10

circle, _, _ = ax.pie(
    values, colors=colors,
    radius=1, startangle=start_angle,
    autopct=format_label, pctdistance=label_position
    )

plt.setp(circle, width=width, edgecolor='white')

ax.legend(circle, text_labels, frameon=False)

plt.tight_layout()

plt.savefig('img/reproducibility_ratio_from_stodden.png')
