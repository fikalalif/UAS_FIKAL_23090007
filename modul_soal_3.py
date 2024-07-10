class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' telah ditambahkan.")

    def dequeue(self):
        if len(self.queue) > 0:
            order = self.queue.pop(0)
            print(f"Order '{order}' telah dihapus.")
            return order
        else:
            print("tidak ada antrian.")
            return None

    def show_queue(self):
        print("antrian : ")
        for i, order in enumerate(self.queue):
            print(f"{i+1}. {order}")

if __name__ == "__main__":
    
    restaurant_queue = RestaurantQueue()
    
    restaurant_queue.enqueue("Order 1")
    restaurant_queue.enqueue("Order 2")
    restaurant_queue.enqueue("Order 3")
    
    restaurant_queue.show_queue()
    
    restaurant_queue.dequeue()
    restaurant_queue.show_queue()
    
    restaurant_queue.dequeue()
    restaurant_queue.dequeue()
    restaurant_queue.dequeue()
    restaurant_queue.show_queue()
