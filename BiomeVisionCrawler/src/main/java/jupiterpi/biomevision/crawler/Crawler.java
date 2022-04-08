package jupiterpi.biomevision.crawler;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Location;
import org.bukkit.block.Biome;
import org.bukkit.entity.Player;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Date;
import java.util.Random;

public class Crawler {
    private Player player;

    private int topCrop = 50;
    private int bottomCrop = 70;

    public Crawler(Player player, int topCrop, int bottomCrop) {
        this.player = player;
        this.topCrop = topCrop;
        this.bottomCrop = bottomCrop;
    }

    public void start() {
        player.sendMessage(ChatColor.GREEN + "Starting crawling!");
    }

    public void step() {
        Location lastLocation = player.getLocation();
        Location location = new Location(Bukkit.getWorld("world"),
                lastLocation.getX() + 5 + new Random().nextInt(5), // 5 to 10
                255,
                lastLocation.getX() + 5 + new Random().nextInt(5) // 5 to 10
        );
        while (!location.getBlock().isSolid()) {
            location.setY(location.getY() - 1);
        }
        location.add(0, 1, 0);
        location.setYaw(new Random().nextInt(360)); // 0 to 360
        location.setPitch(-15 + new Random().nextInt(35)); // -15 to 20
        player.teleport(location);

        Biome biome = location.getWorld().getBiome(location);
        String biomeName = biome.name();

        Bukkit.getScheduler().runTaskLater(BiomeVisionCrawler.plugin, () -> {
            try {
                Robot robot = new Robot();
                Toolkit toolkit = Toolkit.getDefaultToolkit();
                Dimension screenSize = toolkit.getScreenSize();
                Image image = robot.createScreenCapture(new Rectangle(0, bottomCrop, screenSize.width, screenSize.height-(bottomCrop+topCrop)));

                BufferedImage bufferedImage = new BufferedImage(image.getWidth(null), image.getHeight(null), BufferedImage.TYPE_INT_ARGB);
                Graphics2D bGr = bufferedImage.createGraphics();
                bGr.drawImage(image, 0, 0, null);
                bGr.dispose();
                File file = new File(String.format("dataset\\screenshot%s__%s__%s_%s.png", new Date().getTime(), biomeName.toLowerCase(), location.getYaw(), location.getPitch()));
                ImageIO.write(bufferedImage, "png", file);

                // https://stackoverflow.com/questions/13605248/java-converting-image-to-bufferedimage
                // https://stackoverflow.com/questions/464593/how-to-capture-selected-screen-of-other-application-using-java
            } catch (AWTException | IOException e) {
                e.printStackTrace();
            }
        }, 3);
    }

    public void stop() {
        player.sendMessage(ChatColor.RED + "Stopped crawling!");
    }
}