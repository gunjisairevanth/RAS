import datetime

start_time='2021-11-21T10:30:00'
end_time='2021-11-21T11:16:00'
start_time = datetime.datetime.strptime(start_time,"%Y-%m-%dT%H:%M:%S")
end_time = datetime.datetime.strptime(end_time,"%Y-%m-%dT%H:%M:%S")
minutes_difference = (end_time-start_time).total_seconds()/60
print(int(minutes_difference))


# import asyncio
  
  
# async def function_asyc_1():
#     print("function_asyc_1")
#     # return 0

# async def function_asyc_2():
#     print("function_asyc_2")
#     return 0
  
# # to run the above function we'll 
# # use Event Loops these are low 
# # level functions to run async functions
# loop = asyncio.get_event_loop()
# for i in range(0,5):
#     asyncio.gather(function_asyc_1())
# loop.run_forever()



