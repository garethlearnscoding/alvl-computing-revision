import os

class Announcement:
    def __init__(self, department, priority, duration, title): 
        """
        Initialize an Announcement object with department, priority, duration (in seconds), and title.
        """
        self.department = department
        self.priority = priority
        self.duration = duration
        self.title = title

    def __str__(self): 
        """
        Return a human-readable string representation of the announcement.
        Example: "CCA - Science Fair (90s)"
        """
        return f"{self.department} - {self.title} ({self.duration}s)"

    def csv_str(self): 
        """
        Return a CSV-formatted string for writing to file.
        Example: "CCA,High,90,Science Fair"
        """
        return f"{self.department},{self.priority},{self.duration},{self.title}"


class Queue:
    def __init__(self): 
        """
        Initialize an empty queue using a Python list.
        """
        self.head = 0
        self.tail = 0
        self.q = []


    def enqueue(self, item): 
        """
        Add an item to the back of the queue.
        """
        self.q.append(item)
        self.tail += 1
        self.remainingtime -= item.duration

    def dequeue(self): 
        """
        Remove and return the item at the front of the queue, if not empty.
        """
        if self.is_empty:
            return
        else:
            self.head += 1 

    def is_empty(self): 
        """
        Return True if the queue is empty.
        """
        return self.head == self.tail

    def output(self, file): 
        """
        Write each item in the queue to a file, one per line, using its output() method.
        """
        while not self.is_empty():
            annc = [i.csv_str() for i in self.q[self.start:self.end]]
            with open(file,"w") as f:
                f.write("\n".join(annc))
            


        
class AnnouncementScheduler:
    def __init__(self, time_limit=300):
        """
        Initialize the scheduler with an optional time limit (in seconds).
        Sets up data structures for queues and scheduled announcements.
        """ 
        self.time_limit = time_limit
        self.deferred_filename = "deferred_announcement.txt"
        self.announcement_filename = "announcement.txt"
        self.archive_filename = "read_announcements_archived.txt"
        self.scheduled = []
        self.total_time = 0
        self.queues = {'High':Queue(),'Medium':Queue(),'Low':Queue()}
        
    def load_file(self, filename): 
        import csv
        """
        Load Announcement objects from a CSV-formatted file.
        Returns a list of Announcement objects.
        """
        with open(filename) as f:
            data = [Announcement(*list(map(lambda x: int(x) if x.isalpha() else x))) for i in list(csv.reader())]
        return data
    def load_announcements(self):
        """
        Load announcements from both deferred and new announcement files.
        Returns a combined list of Announcement objects.
        """
        return self.load_file(f"./resources/{self.deferred_filename}") + self.load_file(f"./resources/{self.announcement_filename}")

    def categorize(self, announcements):
        """
        Sorts announcements into the internal priority queues
        based on their 'priority' attribute.
        """
        for announcement in announcements:
            self.queues[announcement.priority].enqueue(announcement)

    def process(self):
        """
        Processes announcements from high to low priority queues.
        Adds them to the schedule until the time limit is reached.
        Returns a queue containing deferred announcements.
        """
        defered = Queue()
        queues = [self.queues["High"],self.queues["Medium"],self.queues["Low"]]
        for i in queues:
            while not i.is_empty():
                ann = i.dequeue()
                if ann.duration > self.time_limit -self.total_time:
                    defered.enque(ann)
                else:
                    self.scheduled.append(ann)
                    self.total_time += ann.duration


    def display_schedule(self):
        """
        Prints the list of scheduled announcements and total time used.
        """
        for i in self.scheduled:
            print(i)
        print(self.total_time)

    def archive_scheduled(self):
        """
        Appends the list of scheduled announcements to the archive file.
        Adds a separator line for readability.
        """
        archive = "\n".join([str(i) for i in self.scheduled])
        with open(f"./resources/{self.archive_filename}") as f:
            f.write(archive)

    def save_deferred(self, deferred_queue):
        """
        Writes the deferred announcements to the deferred announcement file
        for processing on the next day.
        """
        deferred_queue.output(f"./resources/{self.deferred_filename}")

    def clear_today_file(self):
        """
        Clears the contents of the new announcement file in preparation for the next day.
        """
        self.scheduled = []
        self.total_time = 0

    def run(self):
        """
        Executes the full announcement scheduling routine:
        1. Load deferred and new announcements
        2. Categorize into priority queues
        3. Schedule announcements within time limit
        4. Display and archive the scheduled announcements
        5. Save unscheduled announcements
        6. Clear today's new announcements
        """
        all_ann = self.load_announcements()
        self.categorize(all_ann)
        deferred = self.process()
        self.display_schedule()
        self.archive_scheduled()
        self.save_deferred(deferred)
        self.clear_today_file()


if __name__ == "__main__":
    scheduler = AnnouncementScheduler()
    scheduler.run()