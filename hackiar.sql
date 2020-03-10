-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-03-2020 a las 19:34:22
-- Versión del servidor: 10.1.38-MariaDB
-- Versión de PHP: 7.3.4

CREATE DATABASE hackiar ;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `hackiar`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nmap`
--


CREATE TABLE `nmap` (
  `ip` varchar(50) NOT NULL,
  `servicio` varchar(50) NOT NULL,
  `puerto` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

