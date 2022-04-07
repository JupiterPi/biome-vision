package jupiterpi.biomevision.crawler;

import org.bukkit.ChatColor;
import org.bukkit.plugin.java.JavaPlugin;

public class BiomeVisionCrawler extends JavaPlugin {
    public static JavaPlugin plugin = null;
    public static CrawlerManager crawlerManager = new CrawlerManager();

    @Override
    public void onEnable() {
        plugin = this;

        getServer().getConsoleSender().sendMessage(ChatColor.GREEN + "[BiomeVision] Crawler enabled");

        getCommand("crawl").setExecutor(new CrawlCommand());

        super.onEnable();
    }

    @Override
    public void onDisable() {
        crawlerManager.stopCrawler();

        getServer().getConsoleSender().sendMessage(ChatColor.RED + "[BiomeVision] Crawler disabled");

        super.onDisable();
    }
}