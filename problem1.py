steps = input("Enter The Steps")
steps_list =list(steps.split()) 

for i in range(len(steps_list)): 
  steps_list[i] = int(steps_list[i]) 

         
highest_step = max(steps_list)
lowest_step = min(steps_list)

average_step = sum(steps_list) / len(steps_list)
sorted_steps = sorted(steps_list,reverse = True)

print (steps_list)
print ("------------")
print ("The Highest Step Is:",highest_step )
print ("------------")
print ("The lowest Step Is:",lowest_step)
print ("------------")
print ("The Average Of The Step Is:",average_step)
print ("------------")
print ("The Steps After Sort Descending Is:",sorted_steps)