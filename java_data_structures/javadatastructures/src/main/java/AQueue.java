import java.util.HashMap;

public abstract class AQueue {

    abstract boolean isEmpty();

    abstract int size();

    abstract AQueue add(int num);

    abstract boolean contains(int num);

    abstract AQueue pop() throws QueueException;

    abstract int peek() throws QueueException;

    /**
     * {@inheritDoc}
     */
    @Override
    public abstract boolean equals(Object obj);
}
