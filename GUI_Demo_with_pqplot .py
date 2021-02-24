#!/usr/bin/env python
# coding: utf-8

# In[36]:


# import libraries
from ipywidgets.widgets import Label, FloatProgress, FloatSlider, Button
from ipywidgets.widgets import Layout, HBox, VBox
from IPython.display import display
import numpy as np
import bqplot as bq
import time
import threading


# In[37]:


# flag to control loop
flag = True

#data to plot
x = np.linspace(0, 2*np.pi, 500)
dx = x[1] - x[0]
y = 1 + np.sin(x)


# In[43]:


# GUI elements

# stop button
b_stop = Button(
    description='Stop',
    icon='stop',
    button_style='warning',
    layout=Layout(width='100px')
)

def stop_click(b):
    global flag
    flag = False
    
b_stop.on_click(stop_click)

#progressbar and label
w1 = FloatProgress(
    value=y[-1],
    min=0,
    max=2,
    description='PV:',
    style={'description_width': 'initial'},
    layout=Layout(width='365px')
)

w2 = Label(
    value=str(np.round(y[-1],2)),
    layout=Layout(margin='0 10px 0 31px')
)

w12 = HBox(
    children=(w1, w2),
    layout=Layout(margin='0 0 0 043px')
)

#slider
wA = FloatSlider(
    value=0,
    min=0,
    max=0.5,
    step=0.01,
    description='Noise:',
    layout=Layout(width='490px', margin='0 0 5px 0')
)

wA


# In[45]:


# Plot elements

#scales
x_sc = bq.LinearScale()
y_sc = bq.LinearScale()

#axis
x_ax = bq.Axis(
    label='x(t)',
    scale=x_sc
)
y_ax = bq.Axis(
    label='y(t)',
    scale=y_sc,
    orientation='vertical'
)

#Lines
Line = bq.Lines(
    x=x,
    y=y,
    scales={'x': x_sc, 'y': y_sc}
)

#Figure
fig = bq.Figure(
    layout=Layout(width='500px', height='300px'),
    axes=[x_ax, y_ax],
    marks=[Line],
    fig_margin=dict(top=10, bottom=40, left=50, right=10)
)

fig


# In[46]:


#Join everything
box = VBox(
    children=(fig, w12, wA),
    layout=Layout(border='solid 2px gray', width='510px')
)
app = VBox(
    children=(b_stop, box)
)


# In[47]:


# Loop function
def work():
        global x
        global y
        
        while flag:
            #get latest value of slider
            A = wA.value
            #delete old values from x and y
            x = np.delete(x, 0)
            y = np.delete(x, 0)
            
            #add new values to x and y
            x  = np.append(x, x[-1]+dx)
            noise = A*np.random.rand()
            y = np.append(y, 1  + np.sin(x[-1]) + noise)
            
            #update progressbar and label
            w1.value = y[-1]
            w2.value = str(np.round(y[-1], 2))
            
            #update plot
            Line.x = x
            Line.y = y
            
            #control cycle speed
            time.sleep(0.05)


# In[48]:


# set the flag to True
flag = True

#create thread
thread = threading.Thread(target=work)

#display the app
display(app)

#start thread
thread.start()


# In[ ]:


#Source: https://www.youtube.com/watch?v=f0WmLo8AVxo


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




