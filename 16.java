import java.util.LinkedList;

public class Logger {
    private LinkedList<Integer> logs;
    private int size;

    public Logger() {
        logs = new LinkedList<Integer>();
        this.size = 0;
    }

    public LinkedList<Integer> getLogs() {
        return logs;
    }

    public void setLogs(LinkedList<Integer> logs) {
        this.logs = logs;
        this.size = logs.size();
    }

    public int getSize() {
        return size;
    }

    public void record(int id) {
        logs.add(id);
        this.size++;
    }

    public int getLast(int i) {
        i = this.size - i;
        return this.logs.get(i);
    }
}
