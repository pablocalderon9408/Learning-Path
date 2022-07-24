""""The test consisted on creating a function that catches the distance between
the first digram and the last one. A digram is a 2 adjacent letters.
Some examples of the output requested:
    "codility" -> -1
    "aaa" -> 1
    "aaakakkmmaak" -> 9
"""
input_given = "aaakakkmmaak"

def solution(input_given):
    # write your code in Python 3.6
    if type(input_given) is str:
        if len(input_given)>2 and len(input_given)<=300000:
            input_given_to_validate = input_given.lower()
            max_distance = 0
            for index in range(0, len(input_given_to_validate)):
                digram = input_given_to_validate[index:index+2]
                for digram2 in range(index + 1, len(input_given_to_validate)):
                    if digram == input_given_to_validate[digram2:digram2+2]:
                        distance = digram2 - index
                        if distance > max_distance:
                            max_distance = distance
            if max_distance == 0:
                return -1
            return max_distance


if __name__ == "__main__":
    ab = solution(input_given)
    print(ab)