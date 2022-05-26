import user
import log

def run():
    temp = user.initial()
    print(temp)
    log.log_file(temp[0], temp[1],temp[3], temp[4])
    

# def run():
#     temp = user.initial()
#     if '1' in temp[0] and '2' in temp[1]:
#         result=user.initial(temp[0], temp[1]), temp[2], temp[3],temp[4]
#     else: 
#         result=user.initial(temp[0], temp[1]), temp[2], temp[3],temp[4]
#     print(result)
#     log.log_file(temp, result)
#     return result
    
        
        
        
    