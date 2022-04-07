package jupiterpi.biomevision.crawler;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;

public class CrawlCommand implements CommandExecutor {
    @Override
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) {
        if (!(sender instanceof Player)) {
            sender.sendMessage("Only available for players. ");
            return true;
        }

        if (BiomeVisionCrawler.crawlerManager.running()) {
            BiomeVisionCrawler.crawlerManager.stopCrawler();
        } else {
            BiomeVisionCrawler.crawlerManager.startCrawler((Player) sender);
        }

        return true;
    }
}
