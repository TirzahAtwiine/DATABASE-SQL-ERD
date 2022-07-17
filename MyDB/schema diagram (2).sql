CREATE TABLE `anime` (
  `id` int PRIMARY KEY,
  `anime_title` text,
  `release_year` text,
  `rating` int
);

CREATE TABLE `characters` (
  `id` int PRIMARY KEY,
  `name` text,
  `c_age` int
);

CREATE TABLE `voice_actors` (
  `id` int PRIMARY KEY,
  `name` text,
  `dob` int,
  `age` int
);

CREATE TABLE `Japanese` (
  `id` int,
  `anime_id` int,
  `characters_id` int,
  `voice_actors_id` int
);

ALTER TABLE `Japanese` ADD FOREIGN KEY (`anime_id`) REFERENCES `anime` (`id`);

ALTER TABLE `Japanese` ADD FOREIGN KEY (`characters_id`) REFERENCES `characters` (`id`);

ALTER TABLE `Japanese` ADD FOREIGN KEY (`voice_actors_id`) REFERENCES `voice_actors` (`id`);
