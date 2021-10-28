"""
Calendar Matching

calendar1 =9:00 -10.30, 12:00-13.00, 16:00-18.00 (9.00 -20.00)
calendar2 =10.00-11.30,12.30-14.30,14:30-15:00, 16:00-17:00 (10.00-18.30)
"""
# O(c1+c2) time | O(c1+c2) space where c1 is length of 1st calendar and c2 is length of 2nd calendar
# daily bounds are constant time because these are only 4 meetings we are adding
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1) #(O(c1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2) # O(c2)
    mergedCalendar = mergedCalendars(updatedCalendar1, updatedCalendar2)
    flattenedCalendar = flattenCalendar(mergedCalendar)
    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)

def updateCalendar(calendar, dailyBounds):
    updateCalendar = calendar[:]  # O(c)
    updateCalendar.insert(0,['0:00', dailyBounds[0]])
    updateCalendar.append([dailyBounds[1], '23:59'])
    return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updateCalendar)) #O(c)

# O(c1 + c2)
def mergedCalendars(calendar1, calendar2):
    merged =[]
    i, j = 0,0
    while i< len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    while i<len(calendar1):
        merged.append(meeting1)
        i += 1
    while j<len(calendar2):
        merged.append(meeting2)
        j += 1
    return merged

# O(c1+c2)
def flattenCalendar(calendar):
    flattened =[calendar[0][:]]
    for i in range(1,len(calendar)):
        currentMeeting = calendar[i]
        previousMeeting = flattened[-1]

        currentStart, currentEnd = currentMeeting
        previousStart, previousEnd = previousMeeting

        if previousEnd >= currentStart:
            newPreviousMeeting =[previousStart, max(previousEnd, currentEnd)]
            flattened[-1] =newPreviousMeeting
        else:
            flattened.append(currentMeeting[:])
    return flattened

# at most O(c1+c2)
def getMatchingAvailabilities(calendar, meetingDuration):
    matchingAvailabilities =[]
    for i in range(1, len(calendar)):
        start = calendar[i -1][1]
        end = calendar[i][0]
        availabilityDuration = end- start
        if availabilityDuration >= meetingDuration:
            matchingAvailabilities.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

# constant time operation because there is only 2 elements
def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(':')))
    return hours * 60 + minutes
# constant time operation because there is only 2 elements
def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursString = str(hours)
    minutesString ='0' +str(mins) if mins < 10 else str(mins)
    return hoursString+":"+minutesString