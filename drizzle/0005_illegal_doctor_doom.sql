CREATE TABLE `cxc_clients` (
	`id` text PRIMARY KEY NOT NULL,
	`record` text NOT NULL,
	`version` integer DEFAULT 1 NOT NULL,
	`updated_at` text,
	`updated_by` text
);
