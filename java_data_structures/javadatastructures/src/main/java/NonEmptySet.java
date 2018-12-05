public class NonEmptySet extends ASet {

    private int data;
    private ASet rest;

    public NonEmptySet(int data, ASet rest) {
        this.data = data;
        this.rest = rest;
    }

    public int getData() {
        return data;
    }

    public ASet getRest() {
        return rest;
    }


    /**
     * {@inheritDoc}
     */
    public boolean isEmpty() {
        return false;
    }

    /**
     * {@inheritDoc}
     */
    public Set add(int num) {
        if(num == getData()){
            return this;
        } else{
            return getRest().add(num);
        }
    }

    /**
     * {@inheritDoc}
     */
    public boolean contains(int num) {
        if(getData() == num){
            return true;
        } else {
            return getRest().contains(num);
        }
    }

    /**
     * Determines if this set is a rest of the other set. If this set is empty, returns true.
     *
     * @param other set to be searched
     * @return true if this set is a rest of the other
     */
    public boolean isSubset(Set other) {
        if(other.contains(getData())) {
            return getRest().isSubset(other);
        } else{
            return false;
        }
    }

    /**
     * {@inheritDoc}
     */
    public Set union(Set other) {
        Set added = other.add(getData());
        return getRest().union(added);
    }

    /**
     * {@inheritDoc}
     */
    public Set intersection(Set other) {
        Set intersect = getRest().intersection(other);

        if(other.contains(getData())){
            intersect.add(getData());
        }
        return intersect;
    }


    /**
     * {@inheritDoc}
     */
    public Set difference(Set other) {

        ASet thisDiff = differenceHelper(other);
        // TODO finish difference method
        //ASet otherDiff = other.differenceHelper(this);





        return null;
    }

    protected ASet differenceHelper(Set other) {
        ASet halfDifference = getRest().differenceHelper(other);
        if(!other.contains(getData())){
            halfDifference.add(getData());
        }
        return halfDifference;
    }

    /**
     * {@inheritDoc}
     */
    public int size() {
        return 1 + getRest().size();
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
            NonEmptySet other = (NonEmptySet) obj;
            if (other.size() != this.size()){
                return false;
            } else {
                return other.isSubset(this) && this.isSubset(other);
            }
    }
}
