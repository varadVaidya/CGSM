# clipping window
xw_max, yw_max = 20, 15
xw_min, yw_min = 5, 1

# viewport window
xv_max, yv_max = 10, 5
xv_min, yv_min = 5, 1

# scaling factors 
sx = (xv_max - xv_min) / (xw_max - xw_min)
sy = (yv_max - yv_min) / (yw_max - yw_min)

# translation factors 
tx = (xw_max*xv_max - xw_min*xv_min) / (xw_max - xw_min)
ty = (yw_max*yv_max - yw_min*yv_min) / (yw_max - yw_min)

########################################################

# Cohen-Sutherland Line Clipping
# top-bottom-right-left

