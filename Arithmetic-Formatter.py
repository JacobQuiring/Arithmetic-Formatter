def arithmetic_arranger(problems, show_answers=False):

    first_line = ''
    second_line = ''
    third_line = ''
    line_length = 0
    count = 0
    answer_line = ''


    if(len(problems) > 5):
        return 'Error: Too many problems.'
    
        

    for x in problems:
        
        #separates the problem into an expression array where elements 0 and 2 are operands and element 1 is the operator
        expression_array = x.split(' ')

        #filtering out non-functional problems
        if not expression_array[0].isnumeric():
            return 'Error: Numbers must only contain digits.'
        elif len(expression_array[0]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif expression_array[1] != '+' and expression_array[1] != '-':
            return "Error: Operator must be '+' or '-'."
        elif not expression_array[2].isnumeric():
             return 'Error: Numbers must only contain digits.'
        elif len(expression_array[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        else:
            #add operator to start second line
            second_line += expression_array[1]
            
            #determine which operand is longer for spacing
            if len(expression_array[0]) > len(expression_array[2]):

                first_line += '  ' + expression_array[0]

                #gauge distances from operator to second operand
                second_line += count_the_spaces(len(expression_array[0]) + 1 - len(expression_array[2])) + expression_array[2]
            
            elif len(expression_array[0]) < len(expression_array[2]):

                #gauge distance from edge of space to first operand
                first_line += count_the_spaces(len(expression_array[2]) + 2 - len(expression_array[0])) + expression_array[0]

                second_line += ' ' + expression_array[2]

            else:

                #default if operands are same length
                first_line += '  ' + expression_array[0]
                second_line += ' ' + expression_array[2]
            
        #determine length of dividing line between equation and solution
        third_line_length = len(first_line) - line_length - 4 * count
        count += 1 

        line_length += third_line_length
        for x in range(third_line_length):
            third_line += '-'

        if show_answers:
            answer = 0
            if expression_array[1] == '+':
                answer = int(expression_array[0]) + int(expression_array[2])
            else:
                answer = int(expression_array[0]) - int(expression_array[2])
            answer_line += count_the_spaces(third_line_length - len(str(answer))) + str(answer)
        
        #space between problems
        first_line += '    '
        second_line += '    '
        third_line += '    '
        answer_line += '    '
    if show_answers:
        return first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip() + '\n' + answer_line.rstrip()
    else:
        return first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()

def count_the_spaces(spaces):
    spaces_arr = []
    for x in range(spaces):
        spaces_arr.append(' ')
    return_spaces = ''.join(spaces_arr)
    return return_spaces

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')