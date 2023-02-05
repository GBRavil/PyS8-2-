
def exam(example):
    while len(example) > 1:
        while '*' in example or '/' in example:
            i = 0
            while i < len(example):
                if example[i] =='/':
                    example[i-1] = float(example[i-1]) / float(example[i+1])
                    example.pop(i)
                    example.pop(i)
                elif example[i] =='*':
                    example[i-1] = float(example[i-1]) * float(example[i+1])
                    example.pop(i)
                    example.pop(i)
                i += 1
        while '+' in example or '-' in example:
            i = 0
            while i < len(example):
                if example[i] =='+':
                    example[i-1] = float(example[i-1]) + float(example[i+1])
                    example.pop(i)
                    example.pop(i)
                elif example[i] =='-':
                    example[i-1] = float(example[i-1]) - float(example[i+1])
                    example.pop(i)
                    example.pop(i)
                i += 1
    


# while len(example) > 1:
#     while '*' in example or '/' in example:
#         i = 0
#         while i < len(example):
#             if example[i] =='/':
#                 example[i-1] = float(example[i-1]) / float(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] =='*':
#                 example[i-1] = float(example[i-1]) * float(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             i += 1
    
#     while '+' in example or '-' in example:
#         i = 0
#         while i < len(example):
#             if example[i] =='+':
#                 example[i-1] = float(example[i-1]) + float(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             elif example[i] =='-':
#                 example[i-1] = float(example[i-1]) - float(example[i+1])
#                 example.pop(i)
#                 example.pop(i)
#             i += 1
    
# view_data(example[0])  