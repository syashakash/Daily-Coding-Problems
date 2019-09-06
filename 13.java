import java.util.HashMap;
import java.util.LinkedList;

public class GetSubstringWithKDistinctChars {
    public String getSubStrWithAtmostkChars(String str, int B) {
        int i=0;
        int j=0;
        int n=str.length();
        int longest=Integer.MIN_VALUE;
        int starti=0;
        HashMap<Character, LinkedList<Integer>> hs = new HashMap<Character,LinkedList<Integer>>();
        while(j < n) {
            System.out.println("j = " + j + " i = " + i + " longest = " + longest);
            Character c = new Character(str.charAt(j));
            System.out.println("Checking for " + c);
            if(hs.containsKey(c)) {
                LinkedList<Integer> q=hs.get(c);
                q.add(j);
                hs.put(c,q);
                System.out.println("add to queue " + c + " at " + j);
                if(longest < j-i+1) {
                    starti=i;
                    longest=j-i+1;
                    System.out.println("start index " + starti + " length " + longest);
                }
            } else {
                if(hs.size() == B) {
                    while(hs.size()==B) {
                        LinkedList p = hs.get(new Character(str.charAt(i)));
                        System.out.println("removed " + p.peek());
                        p.poll();
                        if(p.size()==0) {
                            System.out.println("removed " + str.charAt(i));
                            hs.remove(new Character(str.charAt(i)));
                        } else {
                            hs.put(new Character(str.charAt(i)), p);
                        }
                        i++;
                    }
                    if(hs.size() < B) {
                        LinkedList<Integer> q = new LinkedList<>();
                        q.add(j);
                        System.out.println("created queue for " + c + " at " + j);
                        hs.put(c,q);
                        System.out.println("Added " + c);
                    }
                    if(longest < j-i+1) {
                        starti = i;
                        longest = j - i + 1;
                        System.out.println("start index " + starti + " length " + longest);
                    }
                } else {
                    LinkedList<Integer> q = new LinkedList<>();
                    q.add(j);
                    System.out.println("created queue for " + c + " at " + j);
                    hs.put(c,q);
                    if(longest < j - i + 1) {
                        starti = i;
                        longest = j - i + 1;
                        System.out.println("start index " + starti + " length " + longest);
                    }
                }
            }
            j++;
        }
        System.out.println(starti + " " + longest);
    return str.substring(starti, starti + longest);
    }

}
