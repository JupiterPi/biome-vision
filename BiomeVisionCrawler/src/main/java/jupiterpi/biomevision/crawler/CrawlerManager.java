package jupiterpi.biomevision.crawler;

import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.scheduler.BukkitTask;

public class CrawlerManager {
    private final int betweenTime = 5 * 20;

    private Crawler crawler = null;
    private BukkitTask task = null;

    public void startCrawler(Player player) {
        stopCrawler();
        crawler = new Crawler(player);
        crawler.start();
        task = Bukkit.getServer().getScheduler().runTaskTimer(BiomeVisionCrawler.plugin, crawler::step, 0, betweenTime);
    }

    public void stopCrawler() {
        if (task != null) {
            task.cancel();
            task = null;
        }
        if (crawler != null) {
            crawler.stop();
            crawler = null;
        }
    }

    public boolean running() {
        return task != null;
    }
}