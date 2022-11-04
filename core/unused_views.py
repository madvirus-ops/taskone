          #    """checking for the length of operator 
          #       to determine the kind of opertions to perform
          #   """

            # if op in list(ArithmeticModel.operation_type): #not needed
 
 
 
     # """to check for specific keywords in the given sentence"""
            # elif op not in ArithmeticModel.operation_type:
            #     operators = {"addition","add","sum","multiply","multiplication","times","subtraction","subtract","minus"}
            #     list_int = []
            #     list_str =[]
            #     sentence = op.split(" ")

            #     ##seperating words from numbers
            #     for x in sentence:
            #         if x.isdigit():
            #             list_int.append(x)
            #         list_str.append(x)

            #     ##looping through sentence and comparing to operators
            #     for c in list_str:
            #         if c in operators:
            #             xx = c
            #             if xx in {"addition","add"}:
            #                 res = int(list_int[0]) + int(list_int[1])
            #             elif xx == "subtration":
            #                 res = list_int[0] - list_int[1]
            #             elif xx == "multiplication":
            #                 res = list_int[0] * list_int[1]
            #             else:
            #                 res = "out of range"

                            
            #     response = {"slackUsername":"madvirus","result":res,"operation_type":xx}
            #     # print(response)