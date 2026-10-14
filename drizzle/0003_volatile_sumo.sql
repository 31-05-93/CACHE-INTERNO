ALTER TABLE `cxc_accounts` ADD `status_override` text;--> statement-breakpoint
ALTER TABLE `cxc_accounts` ADD `status_version` integer DEFAULT 1 NOT NULL;