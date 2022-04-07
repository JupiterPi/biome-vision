package jupiterpi.biomevision.crawler;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.entity.Player;

public class Crawler {
    private Player player;

    public Crawler(Player player) {
        this.player = player;
    }

    public void start() {
        player.sendMessage(ChatColor.GREEN + "Starting crawling!");
    }

    public void step() {
        Bukkit.getServer().getConsoleSender().sendMessage("step");
        player.sendMessage("Step.");
    }

    public void stop() {
        player.sendMessage(ChatColor.RED + "Stopped crawling!");
    }
}