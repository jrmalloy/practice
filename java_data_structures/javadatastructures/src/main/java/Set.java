public interface Set {

    /**
     * Determines if a set is empty.
     *
     * @return true if empty, otherwise false.
     */
     boolean isEmpty();

    /**
     * Adds a new element to the set. If set already contains num, return this set.
     *
     * @param num integer to be added to set
     * @return a new set containing all elements of this set, plus n
     */
     Set add(int num);

    /**
     * Determines if set contains num.
     *
     * @param num integer to search for
     * @return true if set contains num, otherwise false.
     */
     boolean contains(int num);

    /**
     * Determines if this set is a subset of the other set. If this set is empty, returns true.
     * @param other set to be searched
     * @return true if this set is a subset of the other
     */
     boolean isSubset(Set other);

    /**
     *
     * @param other set to union
     * @return a new set that is the union of this set and the other
     */
     Set union(Set other);

    /**
     *
     * @param other
     * @return a new set that is the intersection of this set and the other
     */
     Set intersection(Set other);

    /**
     *
     * @param other
     * @return a new set that is the difference of this set and the other
     */
     Set difference(Set other);



    /**
     * Returns number of elements in the set. If set is empty, returns 0.
     *
     * @return number of elements in set.
     */
    public int size();

}
