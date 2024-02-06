s=int(input("enter today\'s steps: "))
# supposing the week's total steps should be 
w=s*7
#imaging 10 steps cost 2 cal
c= s/5
#imaging 10 steps =1m
d= s/10
#monthly distance covered be like 
dc = d*30 #it can be 31 too

def fitness_tracker(w, dc):
    def avg_steps(w):
        return w/7
    
    avg_steps_week = avg_steps(w)
    
    def avg_dis(dc):
         return dc/30
     
    avg_distance_is = avg_dis(dc)
    
    return avg_steps_week, avg_distance_is

avg_steps_week, avg_distance_is= fitness_tracker(w,dc)
print(f"you covered a total distance of {d:.0f} meters.")
print(f"you burned {c:.0f}calories.")
print(f"average steps per week should be{avg_steps_week:.0f}")
print(f"average distance covered by you in a month {avg_distance_is:.0f}")
    


