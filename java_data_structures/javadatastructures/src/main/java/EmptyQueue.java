public class EmptyQueue extends AQueue {

    public EmptyQueue() {
    }

    boolean isEmpty() {
        return true;
    }

    int size() {
        return 0;
    }

    AQueue add(int num) {
        return new NonEmptyQueue(num, this);
    }

    boolean contains(int num) {
        return false;
    }

    AQueue pop() throws QueueException {
        throw new QueueException("Cannot call pop on an empty queue.");
    }

    int peek() throws QueueException {
        throw new QueueException("Cannot call peek on an empty queue.");
    }

    /**
     * {@inheritDoc}
     */
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        return getClass() == obj.getClass();
    }
}
