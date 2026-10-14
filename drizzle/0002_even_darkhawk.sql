CREATE TABLE `cxc_accounts` (
	`id` text PRIMARY KEY NOT NULL,
	`metadata` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `cxc_items` (
	`id` text PRIMARY KEY NOT NULL,
	`report_id` text NOT NULL,
	`account_id` text NOT NULL,
	`record` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `cxc_reports` (
	`id` text PRIMARY KEY NOT NULL,
	`report_date` text NOT NULL,
	`name` text NOT NULL,
	`file_key` text,
	`created_at` text NOT NULL,
	`created_by` text NOT NULL,
	`status` text DEFAULT 'importing' NOT NULL,
	`summary` text DEFAULT '{}' NOT NULL
);
--> statement-breakpoint
CREATE TABLE `cxc_updates` (
	`id` text PRIMARY KEY NOT NULL,
	`account_id` text NOT NULL,
	`body` text NOT NULL,
	`author_id` text,
	`author_email` text,
	`author_label` text NOT NULL,
	`posted_at` text,
	`recorded_at` text NOT NULL,
	`source` text NOT NULL,
	`source_sheet` text,
	`source_row` integer
);
