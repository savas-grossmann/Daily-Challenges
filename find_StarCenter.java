class find_StarCenter {

    /*
        https://leetcode.com/problems/find-center-of-star-graph/
        Given the edges of a Star Graph, find the center Node.
        This is pretty easy because we only need to check the first
        Edges and check which Node they have in common.
        O(1)
     */


    public int find_Center(int[][] edges){
        if(edges[0][1] == edges[1][0] || edges[0][1] == edges[1][1]){
            return edges[0][1];
        } else {
            return edges[0][0];
        }
    }
}