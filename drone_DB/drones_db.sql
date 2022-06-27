-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2022 a las 00:42:54
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `drones_db`
--
CREATE DATABASE IF NOT EXISTS `drones_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `drones_db`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `audit_event_log`
--

CREATE TABLE `audit_event_log` (
  `drone_id` char(100) NOT NULL,
  `battery_level` int(10) NOT NULL,
  `audit_date` datetime NOT NULL DEFAULT current_timestamp(),
  `id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `audit_event_log`
--

INSERT INTO `audit_event_log` (`drone_id`, `battery_level`, `audit_date`, `id`) VALUES
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 11:33:56', 8),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 11:33:56', 9),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 11:33:56', 10),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 11:33:56', 11),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 11:33:56', 12),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 11:33:56', 13),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 11:33:56', 14),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 20, '2022-06-24 11:33:56', 15),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 11:33:56', 16),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 11:33:56', 17),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:30:00', 23),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:30:00', 24),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:30:00', 25),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:30:00', 26),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:30:00', 27),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:30:00', 28),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:30:00', 29),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:30:00', 30),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:30:00', 31),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:30:00', 32),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:33:00', 38),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:33:00', 39),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:33:00', 40),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:33:00', 41),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:33:00', 42),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:33:00', 43),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:33:00', 44),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:33:00', 45),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:33:00', 46),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:33:00', 47),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:36:00', 53),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:36:00', 54),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:36:00', 55),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:36:00', 56),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:36:00', 57),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:36:00', 58),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:36:00', 59),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:36:00', 60),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:36:00', 61),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:36:00', 62),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:39:00', 68),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:39:00', 69),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:39:00', 70),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:39:00', 71),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:39:00', 72),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:39:00', 73),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:39:00', 74),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:39:00', 75),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:39:00', 76),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:39:00', 77),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:42:00', 83),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:42:00', 84),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:42:00', 85),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:42:00', 86),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:42:00', 87),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:42:00', 88),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:42:00', 89),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:42:00', 90),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:42:00', 91),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:42:00', 92),
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 100, '2022-06-24 18:45:00', 98),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 100, '2022-06-24 18:45:00', 99),
('d04f3a24-f255-11ec-be05-43d9ff776750', 100, '2022-06-24 18:45:00', 100),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 23, '2022-06-24 18:45:00', 101),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 90, '2022-06-24 18:45:00', 102),
('f8238360-f17f-11ec-98d8-d71374c94aea', 70, '2022-06-24 18:45:00', 103),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 22, '2022-06-24 18:45:00', 104),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 70, '2022-06-24 18:45:00', 105),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 24, '2022-06-24 18:45:00', 106),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 90, '2022-06-24 18:45:00', 107);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `drone`
--

CREATE TABLE `drone` (
  `serial_number` char(100) NOT NULL,
  `model` char(50) NOT NULL,
  `weight_limit` int(10) UNSIGNED NOT NULL,
  `battery_capacity` int(10) UNSIGNED NOT NULL,
  `state` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `drone`
--

INSERT INTO `drone` (`serial_number`, `model`, `weight_limit`, `battery_capacity`, `state`) VALUES
('d04f39ac-f255-11ec-be02-17d5ec094e9a', 'Middleweight', 250, 100, 'LOADING'),
('d04f3a06-f255-11ec-be04-6bb0ce68c2ac', 'Heavyweight', 490, 100, 'LOADED'),
('d04f3a24-f255-11ec-be05-43d9ff776750', 'Lightweight', 130, 100, 'LOADED'),
('f823823e-f17f-11ec-98d5-57353b2e48f4', 'Cruiserweight', 400, 23, 'LOADING'),
('f8238342-f17f-11ec-98d7-47e0649d92e3', 'Middleweight', 260, 90, 'DELIVERING'),
('f8238360-f17f-11ec-98d8-d71374c94aea', 'Heavyweight', 480, 70, 'RETURNING'),
('f823837e-f17f-11ec-98d9-a7d4c5648dfd', 'Cruiserweight', 480, 22, 'LOADING'),
('f82383ba-f17f-11ec-98db-0f80c70d9b0e', 'Cruiserweight', 380, 70, 'LOADED'),
('f82383d8-f17f-11ec-98dc-fbac941fa328', 'Middleweight', 280, 24, 'LOADING'),
('f8238414-f17f-11ec-98de-9f63865a7e9e', 'Lightweight', 190, 90, 'LOADING');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `load_register`
--

CREATE TABLE `load_register` (
  `load_id` int(10) NOT NULL,
  `loads_list` varchar(1000) NOT NULL,
  `loaded_drone` char(100) NOT NULL,
  `loaded_weight` int(10) NOT NULL,
  `create_date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `load_register`
--

INSERT INTO `load_register` (`load_id`, `loads_list`, `loaded_drone`, `loaded_weight`, `create_date`) VALUES
(8, '[\"43135D38_F2B5\", \"65P8P87_L974Y\", \"65JO75K_F79R4\"]', 'f82383ba-f17f-11ec-98db-0f80c70d9b0e', 330, '2022-06-25 14:34:57'),
(9, '[\"65BK957_579RI\", \"65BK957_579RI\", \"431VC52_J2L4\",\"65P8P87_L974Y\",\"637P85Z_G99P0\"]', 'd04f3a06-f255-11ec-be04-6bb0ce68c2ac', 370, '2022-06-25 14:41:30');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medication`
--

CREATE TABLE `medication` (
  `name` varchar(150) NOT NULL,
  `weight` int(10) UNSIGNED NOT NULL,
  `code` char(100) NOT NULL,
  `image` longblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `medication`
--

INSERT INTO `medication` (`name`, `weight`, `code`, `image`) VALUES
('Viagra', 10, '43135CF2_F2B5', NULL),
('Valtrex', 20, '43135D1A_F2B5', NULL),
('Valium', 30, '43135D38_F2B5', NULL),
('Vicodin', 30, '431VC52_J2L4', NULL),
('Voltaren', 40, '637P85Z_G99P0', NULL),
('Vistaril', 50, '63Y6C52_92P7', NULL),
('Atropine', 150, '659R7GT_FI73G', NULL),
('Atenolol', 150, '65BK957_579RI', NULL),
('Vyvanse', 150, '65JO75K_F79R4', NULL),
('Amoxicillin', 150, '65P8P87_L974Y', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `audit_event_log`
--
ALTER TABLE `audit_event_log`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `drone`
--
ALTER TABLE `drone`
  ADD PRIMARY KEY (`serial_number`);

--
-- Indices de la tabla `load_register`
--
ALTER TABLE `load_register`
  ADD PRIMARY KEY (`load_id`);

--
-- Indices de la tabla `medication`
--
ALTER TABLE `medication`
  ADD PRIMARY KEY (`code`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `audit_event_log`
--
ALTER TABLE `audit_event_log`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=108;

--
-- AUTO_INCREMENT de la tabla `load_register`
--
ALTER TABLE `load_register`
  MODIFY `load_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

DELIMITER $$
--
-- Eventos
--
CREATE DEFINER=`root`@`localhost` EVENT `history_audit_logs` ON SCHEDULE EVERY 3 MINUTE STARTS '2022-06-24 18:30:00' ENDS '2022-06-24 18:46:00' ON COMPLETION PRESERVE DISABLE DO INSERT INTO audit_event_log (drone_id,battery_level) SELECT serial_number,battery_capacity FROM drone$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
