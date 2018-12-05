public class NonEmptyQueue extends AQueue {

    private int data;
    private AQueue rest;

    public NonEmptyQueue(int data, AQueue rest) {
        this.data = data;
        this.rest = rest;
    }

    public int getData() {
        return data;
    }

    public AQueue getRest() {
        return rest;
    }


    boolean isEmpty() {
        return false;
    }

    int size() {
        return 1 + getRest().size();
    }

    AQueue add(int num) {
        return new NonEmptyQueue(num, this);
    }

    boolean contains(int num) {
        if(num == getData()) {
            return true;
        } else {
            return getRest().contains(num);
        }
    }

    AQueue pop() throws QueueException {
        return getRest();
    }

    int peek() throws QueueException {
        return getData();
    }

    /**
     * {@inheritDoc}
     */
    public boolean equals(Object obj) {
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        NonEmptyQueue other = (NonEmptyQueue) obj;
        if (other.size() != this.size()){
            return false;
        }

        return getData() == other.getData() && getRest().equals(other.getRest());
    }
}
