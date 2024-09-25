def factorizar ( number : int ) -> int:
    counter=1
    facto=1
    while counter <= number:
        facto*=counter
        counter+=1
    return facto
