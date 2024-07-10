from modul_soal_3 import RestaurantQueue

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