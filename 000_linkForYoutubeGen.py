videoTime = "14:47:45"

def convertStringTimeToSeconds(timeString):
   # h, m, s = timeString.split(':')
   # return ((int)h*60*60)
#    return(int(x) for x in timeString.split(':'))
    x = list(map(int, timeString.split(':')))
    a = x[0] * 60 * 60
    b = x[1] * 60 
    c = (int)(x[2])
    final = a+b+c
    link = "https://www.youtube.com/watch?v=nLRL_NcnK-4"
    return( f"{link}&t={final}s")

print(convertStringTimeToSeconds(videoTime))