
public abstract class ASet implements Set {

    /**
     * {@inheritDoc}
     */
    public abstract boolean isEmpty();

    /**
     * {@inheritDoc}
     */
    public abstract Set add(int num);

    /**
     * {@inheritDoc}
     */
    public abstract boolean contains(int num);

    /**
     * {@inheritDoc}
     */
    public abstract boolean isSubset(Set other);

    /**
     * {@inheritDoc}
     */
    public abstract Set union(Set other);

    /**
     * {@inheritDoc}
     */
    public abstract Set intersection(Set other);

    /**
     * {@inheritDoc}
     */
    public abstract Set difference(Set other);

    protected abstract ASet differenceHelper(Set other);


    /**
     * {@inheritDoc}
     */
    public abstract int size();

    /**
     * {@inheritDoc}
     */
    @Override
    public abstract boolean equals(Object obj);
}
