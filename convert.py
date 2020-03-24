def bin2dec(value):

    indice = len(value) - 1
    dec = 0

    if indice > 8:
        return "Limite estourado!"
    else:
        for i in value:
          dec += int(i) * (pow(2,indice))
          indice -= 1
        
        return dec

