# arr = [2,3,4,5,6]

# def swap(arr, a, b):
# 	temp = arr[a]
# 	arr[a] = arr[b]
# 	arr[b] = temp

# swap(arr, 1, 2)
# # print(arr)

# def f1(a, b):
# 	return a+b, a-b

# def f2(c, d):
# 	return c*d

# result1 = f2(f1(3,6)[0], 4)
# result2 = f2(*f1(3,6))
# print(result1)
# print(result2)

# k = -4
# print(bin(k))

# for i in bin(k)[:: -1]:
# 	print(type(i))

# def make_adder(n):
# 	def adder(k):
# 		return k+n
# 	return adder

# print(make_adder(3)(make_adder(3)(4)))


# print(0^3)

def say_scores(score0, score1):

    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(prev_leader=None):

    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != prev_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):

    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say

h0 = announce_lead_changes(1)
h1 = h0(1,3)
h2 = h1(2,4)

print(h0)
print(h1)
print(h2)
