

public class EmptySet extends ASet {
    /**
     * {@inheritDoc}
     */
    public boolean isEmpty() {
        return true;
    }

    /**
     * {@inheritDoc}
     */
    public Set add(int num) {
        return new NonEmptySet(num, this);
    }

    /**
     * {@inheritDoc}
     */
    public boolean contains(int num) {
        return false;
    }

    /**
     * {@inheritDoc}
     */
    public boolean isSubset(Set other) {
        return true;
    }

    /**
     * {@inheritDoc}
     */
    public Set union(Set other) {
        return other;
    }

    /**
     * {@inheritDoc}
     */
    public Set intersection(Set other) {
        return new EmptySet();
    }

    /**
     * {@inheritDoc}
     */
    public Set difference(Set other) {
        return other;
    }

    protected Set differenceHelper(Set other) {
        return new EmptySet();
    }

    /**
     * {@inheritDoc}
     */
    public int size() {
        return 0;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public boolean equals(Object obj) {
            if (obj == null) {
                return false;
            }
            return getClass() == obj.getClass();
    }
}
