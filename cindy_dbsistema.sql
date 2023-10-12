-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-10-2021 a las 03:45:27
-- Versión del servidor: 10.4.20-MariaDB
-- Versión de PHP: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cindy_dbsistema`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbldocente`
--

CREATE TABLE `tbldocente` (
  `PKIdentificacion` varchar(10) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Apellido` varchar(100) NOT NULL,
  `Telefono` varchar(10) NOT NULL,
  `FKId_tblSexo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbldocente`
--

INSERT INTO `tbldocente` (`PKIdentificacion`, `Nombre`, `Apellido`, `Telefono`, `FKId_tblSexo`) VALUES
('1002234549', 'Diana ', 'Ruiz Diaz', '31047589', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblestudiante`
--

CREATE TABLE `tblestudiante` (
  `PKIdentificacion` varchar(10) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Apellidos` varchar(100) NOT NULL,
  `Telefono` varchar(10) DEFAULT NULL,
  `FKId_tblsexo` int(11) NOT NULL,
  `FKId_tblgrado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblestudiante`
--

INSERT INTO `tblestudiante` (`PKIdentificacion`, `Nombre`, `Apellidos`, `Telefono`, `FKId_tblsexo`, `FKId_tblgrado`) VALUES
('100', 'Oscar', 'Mesa', '123', 1, 1),
('12', 'Mario', 'Montoya', '01', 1, 1),
('13', 'elchim', 'bolitoss', '11', 2, 5),
('15', 'MarioDb', 'wtf', '123', 2, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblgestion_alumno`
--

CREATE TABLE `tblgestion_alumno` (
  `PKId` int(11) NOT NULL,
  `FKIdentificacion` varchar(10) NOT NULL,
  `FKId_tblPeriodo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblgestion_alumno`
--

INSERT INTO `tblgestion_alumno` (`PKId`, `FKIdentificacion`, `FKId_tblPeriodo`) VALUES
(13, '13', 2),
(15, '15', 3),
(100, '100', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblgestion_docente`
--

CREATE TABLE `tblgestion_docente` (
  `PKId` int(11) NOT NULL,
  `FKIdentificacion_tblDocente` varchar(10) NOT NULL,
  `FKId_tblGrado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblgestion_docente`
--

INSERT INTO `tblgestion_docente` (`PKId`, `FKIdentificacion_tblDocente`, `FKId_tblGrado`) VALUES
(1, '1002234549', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblgrado`
--

CREATE TABLE `tblgrado` (
  `PKId` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblgrado`
--

INSERT INTO `tblgrado` (`PKId`, `Descripcion`) VALUES
(1, 'Primero'),
(2, 'Segundo '),
(3, 'Tercero'),
(4, 'Cuarto'),
(5, 'Quinto'),
(6, 'Sexto'),
(7, 'Septimo '),
(8, 'Octavo'),
(9, 'Noveno '),
(10, 'Decimo'),
(11, 'Once');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblmaterias`
--

CREATE TABLE `tblmaterias` (
  `PKId` varchar(5) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblmaterias`
--

INSERT INTO `tblmaterias` (`PKId`, `Descripcion`) VALUES
('E01', 'Edu. Fisica'),
('E02', 'Quimica'),
('E03', 'Matematica'),
('E04', 'Física'),
('E05', 'Tecnologia'),
('E06', 'Español'),
('E07', 'Etica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblperiodo`
--

CREATE TABLE `tblperiodo` (
  `PKId` int(11) NOT NULL,
  `Descripcion` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblperiodo`
--

INSERT INTO `tblperiodo` (`PKId`, `Descripcion`) VALUES
(1, 'Primer Periodo'),
(2, 'Segundo Periodo'),
(3, 'Tercer Periodo'),
(4, 'Cuarto Periodo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblsexo`
--

CREATE TABLE `tblsexo` (
  `PKId` int(11) NOT NULL,
  `Descripcion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tblsexo`
--

INSERT INTO `tblsexo` (`PKId`, `Descripcion`) VALUES
(1, 'Masculino'),
(2, 'Femenino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_det_gestion_alumno`
--

CREATE TABLE `tbl_det_gestion_alumno` (
  `PKId` int(11) NOT NULL,
  `FKId_tblGestion_Alumno` int(11) NOT NULL,
  `FKId_tblMaterias` varchar(5) NOT NULL,
  `Nota_final` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tbl_det_gestion_alumno`
--

INSERT INTO `tbl_det_gestion_alumno` (`PKId`, `FKId_tblGestion_Alumno`, `FKId_tblMaterias`, `Nota_final`) VALUES
(29, 13, 'E02', 5),
(30, 100, 'E01', 1),
(31, 15, 'E04', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tbl_det_gestion_docente`
--

CREATE TABLE `tbl_det_gestion_docente` (
  `PKId` int(11) NOT NULL,
  `FKId_tblGestion_Docente` int(11) NOT NULL,
  `FKId_tblMaterias` varchar(5) NOT NULL,
  `Horario` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tbldocente`
--
ALTER TABLE `tbldocente`
  ADD PRIMARY KEY (`PKIdentificacion`),
  ADD KEY `FKId_tblSexo` (`FKId_tblSexo`);

--
-- Indices de la tabla `tblestudiante`
--
ALTER TABLE `tblestudiante`
  ADD PRIMARY KEY (`PKIdentificacion`),
  ADD KEY `FKId_tblsexo` (`FKId_tblsexo`),
  ADD KEY `FKId_tblgrado` (`FKId_tblgrado`);

--
-- Indices de la tabla `tblgestion_alumno`
--
ALTER TABLE `tblgestion_alumno`
  ADD PRIMARY KEY (`PKId`),
  ADD KEY `FKIdentificacion` (`FKIdentificacion`),
  ADD KEY `FKId_tblPeriodo` (`FKId_tblPeriodo`);

--
-- Indices de la tabla `tblgestion_docente`
--
ALTER TABLE `tblgestion_docente`
  ADD PRIMARY KEY (`PKId`),
  ADD KEY `FKIdentificacion_tblDocente` (`FKIdentificacion_tblDocente`),
  ADD KEY `FKId_tblGrado` (`FKId_tblGrado`);

--
-- Indices de la tabla `tblgrado`
--
ALTER TABLE `tblgrado`
  ADD PRIMARY KEY (`PKId`);

--
-- Indices de la tabla `tblmaterias`
--
ALTER TABLE `tblmaterias`
  ADD PRIMARY KEY (`PKId`);

--
-- Indices de la tabla `tblperiodo`
--
ALTER TABLE `tblperiodo`
  ADD PRIMARY KEY (`PKId`);

--
-- Indices de la tabla `tblsexo`
--
ALTER TABLE `tblsexo`
  ADD PRIMARY KEY (`PKId`);

--
-- Indices de la tabla `tbl_det_gestion_alumno`
--
ALTER TABLE `tbl_det_gestion_alumno`
  ADD PRIMARY KEY (`PKId`),
  ADD KEY `FKId_tblGestion_Alumno` (`FKId_tblGestion_Alumno`),
  ADD KEY `FKId_tblMatrias` (`FKId_tblMaterias`);

--
-- Indices de la tabla `tbl_det_gestion_docente`
--
ALTER TABLE `tbl_det_gestion_docente`
  ADD PRIMARY KEY (`PKId`),
  ADD KEY `FKId_tblGestion_Docente` (`FKId_tblGestion_Docente`),
  ADD KEY `FKId_tblMaterias` (`FKId_tblMaterias`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tblgestion_docente`
--
ALTER TABLE `tblgestion_docente`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tblgrado`
--
ALTER TABLE `tblgrado`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `tblperiodo`
--
ALTER TABLE `tblperiodo`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tblsexo`
--
ALTER TABLE `tblsexo`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tbl_det_gestion_alumno`
--
ALTER TABLE `tbl_det_gestion_alumno`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `tbl_det_gestion_docente`
--
ALTER TABLE `tbl_det_gestion_docente`
  MODIFY `PKId` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tbldocente`
--
ALTER TABLE `tbldocente`
  ADD CONSTRAINT `tbldocente_ibfk_1` FOREIGN KEY (`FKId_tblSexo`) REFERENCES `tblsexo` (`PKId`);

--
-- Filtros para la tabla `tblestudiante`
--
ALTER TABLE `tblestudiante`
  ADD CONSTRAINT `tblestudiante_ibfk_1` FOREIGN KEY (`FKId_tblsexo`) REFERENCES `tblsexo` (`PKId`),
  ADD CONSTRAINT `tblestudiante_ibfk_2` FOREIGN KEY (`FKId_tblgrado`) REFERENCES `tblgrado` (`PKId`);

--
-- Filtros para la tabla `tblgestion_alumno`
--
ALTER TABLE `tblgestion_alumno`
  ADD CONSTRAINT `tblgestion_alumno_ibfk_1` FOREIGN KEY (`FKIdentificacion`) REFERENCES `tblestudiante` (`PKIdentificacion`),
  ADD CONSTRAINT `tblgestion_alumno_ibfk_2` FOREIGN KEY (`FKId_tblPeriodo`) REFERENCES `tblperiodo` (`PKId`);

--
-- Filtros para la tabla `tblgestion_docente`
--
ALTER TABLE `tblgestion_docente`
  ADD CONSTRAINT `tblgestion_docente_ibfk_1` FOREIGN KEY (`FKIdentificacion_tblDocente`) REFERENCES `tbldocente` (`PKIdentificacion`),
  ADD CONSTRAINT `tblgestion_docente_ibfk_2` FOREIGN KEY (`FKId_tblGrado`) REFERENCES `tblgrado` (`PKId`);

--
-- Filtros para la tabla `tbl_det_gestion_alumno`
--
ALTER TABLE `tbl_det_gestion_alumno`
  ADD CONSTRAINT `tbl_det_gestion_alumno_ibfk_1` FOREIGN KEY (`FKId_tblMaterias`) REFERENCES `tblmaterias` (`PKId`),
  ADD CONSTRAINT `tbl_det_gestion_alumno_ibfk_2` FOREIGN KEY (`FKId_tblGestion_Alumno`) REFERENCES `tblgestion_alumno` (`PKId`);

--
-- Filtros para la tabla `tbl_det_gestion_docente`
--
ALTER TABLE `tbl_det_gestion_docente`
  ADD CONSTRAINT `tbl_det_gestion_docente_ibfk_1` FOREIGN KEY (`FKId_tblGestion_Docente`) REFERENCES `tblgestion_docente` (`PKId`),
  ADD CONSTRAINT `tbl_det_gestion_docente_ibfk_2` FOREIGN KEY (`FKId_tblMaterias`) REFERENCES `tblmaterias` (`PKId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
