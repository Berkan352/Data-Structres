# linked list
# 1. create a node
# 2. create a linked list
# 3. add a node to the linked list
# 4. print the linked list
# 5. delete a node from the linked list
# 6. reverse the linked list
# 7. find the middle node of the linked list
# 8. find the nth node from the end of the linked list
# 9. find the nth node from the beginning of the linked list
# 10. find the length of the linked list
# 11. find the sum of the linked list
# 12. find the maximum value of the linked list
# 13. find the minimum value of the linked list
# 14. find the average value of the linked list
# 15. find the median value of the linked list
# 16. find the mode value of the linked list
# 17. find the standard deviation of the linked list
# 18. find the variance of the linked list
# 19. find the skewness of the linked list
# 20. find the kurtosis of the linked list
# 21. find the covariance of the linked list
# 22. find the correlation of the linked list
# 23. find the percentile of the linked list
# 24. find the quartile of the linked list
# 25. find the decile of the linked list
# 26. find the percentile rank of the linked list


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while node.next:
                node = node.next
            node.next = Node(data)
        self.length += 1

    def remove(self, data):
        if self.root is None:
            return
        if self.root.data == data:
            self.root = self.root.next
            return
        node = self.root
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                break
            node = node.next

    def reverse(self):
        prev = None
        node = self.root
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.root = prev

    def middle(self):
        slow = self.root
        fast = self.root
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def nth_from_end(self, n):
        node = self.root
        for _ in range(self.length - n):
            node = node.next
        return node.data

    def nth_from_beginning(self, n):
        node = self.root
        for _ in range(n-1):
            node = node.next
        return node.data

    def sum_of_list(self):
        total = 0
        node = self.root
        for _ in range(self.length):
            total += node.data
            node = node.next
        return total

    def max_value_of_list(self):
        node = self.root
        max_value = node.data
        for _ in range(self.length):
            if node.data > max_value:
                max_value = node.data
            node = node.next
        return max_value

    def min_value_of_list(self):
        node = self.root
        min_value = node.data
        for _ in range(self.length):
            if node.data < min_value:
                min_value = node.data
            node = node.next
        return min_value

    def average_value_of_list(self):
        return self.sum_of_list() / self.length

    def median_value_of_list(self):
        if self.length % 2 == 0:
            return (self.nth_from_beginning(self.length // 2) + self.nth_from_beginning(self.length // 2 + 1)) / 2
        else:
            return self.nth_from_beginning(self.length // 2 + 1)

    def mode_value_of_list(self):
        node = self.root
        mode = node.data
        mode_count = 1
        for _ in range(self.length-1):
            node = node.next
            if node.data == mode:
                mode_count += 1
            else:
                mode_count -= 1
            if mode_count == 0:
                mode = node.data
                mode_count = 1
        return mode

    def standard_deviation_of_list(self):
        avg = self.average_value_of_list()
        node = self.root
        total = 0
        for _ in range(self.length):
            total += (node.data - avg) ** 2
            node = node.next
        return (total / self.length) ** 0.5

    def variance_of_list(self):
        return self.standard_deviation_of_list() ** 2

    def skewness_of_list(self):
        avg = self.average_value_of_list()
        node = self.root
        total = 0
        for _ in range(self.length):
            total += (node.data - avg) ** 3
            node = node.next
        return total / (self.length * self.standard_deviation_of_list() ** 3)

    def kurtosis_of_list(self):
        avg = self.average_value_of_list()
        node = self.root
        total = 0
        for _ in range(self.length):
            total += (node.data - avg) ** 4
            node = node.next
        return total / (self.length * self.standard_deviation_of_list() ** 4)

    def covariance_of_list(self, other):
        avg1 = self.average_value_of_list()
        avg2 = other.average_value_of_list()
        node1 = self.root
        node2 = other.root
        total = 0
        for _ in range(self.length):
            total += (node1.data - avg1) * (node2.data - avg2)
            node1 = node1.next
            node2 = node2.next
        return total / self.length

    def correlation_of_list(self, other):
        return self.covariance_of_list(other) / (self.standard_deviation_of_list() * other.standard_deviation_of_list())

    def percentile_of_list(self, p):
        return self.nth_from_beginning(int(self.length * p / 100))

    def quartile_of_list(self, q):
        return self.nth_from_beginning(int(self.length * q / 4))

    def decile_of_list(self, d):
        return self.nth_from_beginning(int(self.length * d / 10))

    def percentile_rank_of_list(self, x):
        node = self.root
        count = 0
        for _ in range(self.length):
            if node.data <= x:
                count += 1
            node = node.next
        return count / self.length * 100

    def print(self):
        node = self.root
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

if __name__ == '__main__':

    liste=LinkedList()

    for i in range(10):
        liste.add(i)

    liste.print()

    #liste.reverse()

    print(liste.middle())

    liste.print()

    print(liste.nth_from_end(4))

    print(liste.nth_from_beginning(4))

    print(liste.sum_of_list())

    print(liste.max_value_of_list())

    print(liste.min_value_of_list())

    print(liste.average_value_of_list())

    print(liste.median_value_of_list())

    print(liste.mode_value_of_list())

    print(liste.standard_deviation_of_list())

    print(liste.variance_of_list())

    print(liste.skewness_of_list())

    print(liste.kurtosis_of_list())

    liste2=LinkedList()

    for i in range(10):
        liste2.add(i*2)

    print(liste.covariance_of_list(liste2))

    print(liste.correlation_of_list(liste2))

    print(liste.percentile_of_list(50))

    print(liste.quartile_of_list(2))

    print(liste.decile_of_list(5))

    print(liste.percentile_rank_of_list(5))


