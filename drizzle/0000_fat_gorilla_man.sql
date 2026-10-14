CREATE TABLE `okr_audit` (
	`id` text PRIMARY KEY NOT NULL,
	`at` text NOT NULL,
	`actor_id` text NOT NULL,
	`actor_email` text NOT NULL,
	`operation` text NOT NULL,
	`record_id` text NOT NULL,
	`before` text,
	`after` text
);
--> statement-breakpoint
CREATE TABLE `okr_departments` (
	`id` text PRIMARY KEY NOT NULL,
	`name` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `okr_members` (
	`email` text PRIMARY KEY NOT NULL,
	`user_id` text,
	`department_id` text,
	`role` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `okr_objectives` (
	`id` text PRIMARY KEY NOT NULL,
	`department_id` text NOT NULL,
	`period` text NOT NULL,
	`title` text NOT NULL,
	`kr` text NOT NULL,
	`type` text NOT NULL,
	`target` real NOT NULL,
	`weight` real NOT NULL,
	`achieved` real DEFAULT 0 NOT NULL,
	`notes` text DEFAULT '' NOT NULL,
	`comments` text DEFAULT '' NOT NULL,
	`person` text DEFAULT '' NOT NULL,
	`position` text DEFAULT '' NOT NULL,
	`manager` text DEFAULT '' NOT NULL,
	`source_file` text,
	`source_row` integer,
	`version` integer DEFAULT 1 NOT NULL,
	`updated_at` text,
	`updated_by` text
);
--> statement-breakpoint
CREATE TABLE `okr_periods` (
	`id` text PRIMARY KEY NOT NULL,
	`department_id` text NOT NULL,
	`period` text NOT NULL,
	`closed` integer DEFAULT 0 NOT NULL,
	`source_file` text,
	`original_total` real,
	`source_snapshot` text
);
--> statement-breakpoint
CREATE TABLE `okr_settings` (
	`key` text PRIMARY KEY NOT NULL,
	`value` text NOT NULL
);
