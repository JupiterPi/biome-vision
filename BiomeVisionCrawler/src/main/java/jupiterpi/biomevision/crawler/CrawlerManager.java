package jupiterpi.biomevision.crawler;

import org.bukkit.Bukkit;
import org.bukkit.entity.Player;
import org.bukkit.scheduler.BukkitTask;

public class CrawlerManager {
    private final int betweenTime = 30;

    private Crawler crawler = null;
    private BukkitTask task = null;

    public void startCrawler(Player player, int topCrop, int bottomCrop) {
        stopCrawler();
        crawler = new Crawler(player, topCrop, bottomCrop);
        crawler.start();
        task = Bukkit.getServer().getScheduler().runTaskTimer(BiomeVisionCrawler.plugin, crawler::step, 30, betweenTime);
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